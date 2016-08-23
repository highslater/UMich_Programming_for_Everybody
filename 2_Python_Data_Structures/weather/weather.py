"""Use the Weather API from the weather underground.

{
  "response": {
  "version":"0.1",
  "termsofService":"http://www.wunderground.com/weather/api/d/terms.html",
  "features": {
  "conditions": 1
  }
    }
  , "current_observation": {
        "image": {
        "url":"http://icons.wxug.com/graphics/wu2/logo_130x80.png",
        "title":"Weather Underground",
        "link":"http://www.wunderground.com"
        },
        "display_location": {
        "full":"North Grafton, MA",
        "city":"North Grafton",
        "state":"MA",
        "state_name":"Massachusetts",
        "country":"US",
        "country_iso3166":"US",
        "zip":"01536",
        "magic":"1",
        "wmo":"99999",
        "latitude":"42.23019409",
        "longitude":"-71.70266724",
        "elevation":"99.00000000"
        },
        "observation_location": {
        "full":"Snow Rd, North Grafton, Massachusetts",
        "city":"Snow Rd, North Grafton",
        "state":"Massachusetts",
        "country":"US",
        "country_iso3166":"US",
        "latitude":"42.232658",
        "longitude":"-71.699448",
        "elevation":"325 ft"
        },
        "estimated": {
        },
        "station_id":"KMANORTH49",
        "observation_time":"Last Updated on July 27, 12:02 AM EDT",
        "observation_time_rfc822":"Wed, 27 Jul 2016 00:02:56 -0400",
        "observation_epoch":"1469592176",
        "local_time_rfc822":"Wed, 27 Jul 2016 00:04:18 -0400",
        "local_epoch":"1469592258",
        "local_tz_short":"EDT",
        "local_tz_long":"America/New_York",
        "local_tz_offset":"-0400",
        "weather":"Clear",
        "temperature_string":"70.0 F (21.1 C)",
        "temp_f":70.0,
        "temp_c":21.1,
        "relative_humidity":"75%",
        "wind_string":"Calm",
        "wind_dir":"SE",
        "wind_degrees":135,
        "wind_mph":0.0,
        "wind_gust_mph":0,
        "wind_kph":0,
        "wind_gust_kph":0,
        "pressure_mb":"1014",
        "pressure_in":"29.93",
        "pressure_trend":"+",
        "dewpoint_string":"62 F (16 C)",
        "dewpoint_f":62,
        "dewpoint_c":16,
        "heat_index_string":"NA",
        "heat_index_f":"NA",
        "heat_index_c":"NA",
        "windchill_string":"NA",
        "windchill_f":"NA",
        "windchill_c":"NA",
        "feelslike_string":"70.0 F (21.1 C)",
        "feelslike_f":"70.0",
        "feelslike_c":"21.1",
        "visibility_mi":"10.0",
        "visibility_km":"16.1",
        "solarradiation":"--",
        "UV":"0","precip_1hr_string":"0.00 in ( 0 mm)",
        "precip_1hr_in":"0.00",
        "precip_1hr_metric":" 0",
        "precip_today_string":"0.00 in (0 mm)",
        "precip_today_in":"0.00",
        "precip_today_metric":"0",
        "icon":"clear",
        "icon_url":"http://icons.wxug.com/i/c/k/nt_clear.gif",
        "forecast_url":"http://www.wunderground.com/US/MA/North_Grafton.html",
        "history_url":"http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KMANORTH49",
        "ob_url":"http://www.wunderground.com/cgi-bin/findweather/getForecast?query=42.232658,-71.699448",
        "nowcast":""
    }
}

"""

import urllib2
import json
f = urllib2.urlopen(
    'http://api.wunderground.com/api/27448dfd2a34cb97/'
    'astronomy/geolookup/conditions/forecast/forecast10day/almanac/'
    'q/MA/North_Grafton.json'
)
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
temp_ff = parsed_json['current_observation']['feelslike_f']
temp_c = parsed_json['current_observation']['temp_c']
temp_fc = parsed_json['current_observation']['feelslike_c']
weather = parsed_json['current_observation']['weather']

latLocation = (
    parsed_json['current_observation']['observation_location']['latitude']
)
lngLocation = (
    parsed_json['current_observation']['observation_location']['longitude']
)

moon = parsed_json['moon_phase']['phaseofMoon']
sunriseh = parsed_json['sun_phase']['sunrise']['hour']
sunrisem = parsed_json['sun_phase']['sunrise']['minute']
sunseth = int(parsed_json['sun_phase']['sunset']['hour'])
if sunseth > 12:
    sunseth = sunseth - 12

sunsetm = parsed_json['sun_phase']['sunset']['minute']
moon = parsed_json['moon_phase']['phaseofMoon']

print "Latitude is: %s" % (latLocation)
print "Longitude is: %s" % (lngLocation)
print "Current weather in %s is: %s" % (location, weather)
print "Current temperature is: %s F, Feels like: %s F" % (temp_f, temp_ff)
print "Current temperature is: %s  C, Feels like: %s C" % (temp_c, temp_fc)
print "Current Moon Phase is: %s" % (moon)
print "The sun rose at %s:%s am" % (sunriseh, sunrisem)
print "and will set at %s:%s pm" % (sunseth, sunsetm)
f.close()
