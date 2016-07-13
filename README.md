# Wifi-analyser-Pi

![gadgets](https://raw.githubusercontent.com/takamatsu-shyo/Wifi-analyser-Pi/master/image/gadgets.jpg)

This is a WiFi analyzer based on Raspberry Pi and a WiFi dongle. After two steps, online scanning and offline analysis, MAC addresses are dropped in Google Map. For security reason, a part of the address is masked but technically any information in `iwlist scan` can be extracted by modified the offline analysis script.

In short, you will get like this.

![WiFi map](https://raw.githubusercontent.com/takamatsu-shyo/Wifi-analyser-Pi/master/image/screenshot_map.png)

https://drive.google.com/open?id=1TacgweZSb1_Dr1nuRZAWz2uydWM&usp=sharing

## Workflow

![flow](https://raw.githubusercontent.com/takamatsu-shyo/Wifi-analyser-Pi/master/image/flow.png)

1. loop.sh is continuously execute `iwlist scan` then save output to files. In the meanwhile, geolocation is recorded by GPS Logger.

2. extract.sh processes the files so that desired information is picked up.

3. timeConverter.py read ISO8601 format then out the epoch time to prepare next combining step

4. geoInsert.py append geolocation to information from the Pi

5. Processed information is uploaded to Google drive then read it from Google MyMaps

For more details, please refer wiki page.
