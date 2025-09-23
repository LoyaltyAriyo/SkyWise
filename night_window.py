# day3_night_window.py
from __future__ import annotations

import yaml
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import EarthLocation
from astroplan import Observer


@dataclass
class SiteConfig:
    name: str
    latitude: float
    longitude: float
    elevation: float
    timezone: str


def load_config(path: str = "config.yaml") -> tuple[SiteConfig, str]:
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)

    s = cfg["site"]
    site = SiteConfig(
        name=s["name"],
        latitude=float(s["latitude"]),
        longitude=float(s["longitude"]),
        elevation=float(s["elevation"]),
        timezone=s["timezone"],
    )
    return site, str(cfg["observation_date"])


def main() -> None:
    site, date_str = load_config()
    tz = ZoneInfo(site.timezone)

    # Anchor at *local noon* on the chosen date to avoid midnight edge cases
    local_noon = datetime.fromisoformat(f"{date_str}T12:00:00").replace(tzinfo=tz)
    t0 = Time(local_noon)  # Astropy Time (UTC internally)

    # Build the Observer for the site
    loc = EarthLocation(lat=site.latitude * u.deg,
                        lon=site.longitude * u.deg,
                        height=site.elevation * u.m)
    observer = Observer(location=loc, name=site.name, timezone=site.timezone)

    # Solar events
    sunset = observer.sun_set_time(t0, which="next")
    sunrise = observer.sun_rise_time(t0, which="next")
    astro_evening = observer.twilight_evening_astronomical(t0, which="next")   # sun < -18°
    astro_morning = observer.twilight_morning_astronomical(t0, which="next")

    def fmt(t: Time) -> str:
        return t.to_datetime(timezone=tz).strftime("%H:%M")

    print(f"Site: {site.name} ({site.latitude:.4f}, {site.longitude:.4f})  tz={site.timezone}")
    print(f"Date: {date_str}")
    print(f"Sunset: {fmt(sunset)}  | Astronomical night starts: {fmt(astro_evening)}")
    print(f"Astronomical night ends: {fmt(astro_morning)}  | Sunrise: {fmt(sunrise)}")
    print(f"Astronomical night: {fmt(astro_evening)} → {fmt(astro_morning)} ({site.timezone})")


if __name__ == "__main__":
    main()
