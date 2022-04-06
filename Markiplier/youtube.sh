#!/bin/bash
echo 'https://www.youtube.com/youtubei/v1/player?key=${1}&prettyPrint=true'
curl 'https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=true' \
  -H 'authority: www.youtube.com' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"' \
  -H 'sec-ch-ua-full-version-list: " Not A;Brand";v="99.0.0.0", "Chromium";v="99.0.4844.84", "Google Chrome";v="99.0.4844.84"' \
  -H 'content-type: application/json' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36' \
  -H 'sec-ch-ua-arch: "x86"' \
  -H 'sec-ch-ua-full-version: "99.0.4844.84"' \
  -H 'sec-ch-ua-platform-version: "10.0.0"' \
  -H 'x-youtube-client-name: 56' \
  -H 'x-youtube-client-version: 1.20220403.00.00' \
  -H 'sec-ch-ua-bitness: "64"' \
  -H 'sec-ch-ua-model: ' \
  -H 'x-goog-visitor-id: CgtOV3hHUHJvczNkNCijjrSSBg%3D%3D' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'accept: */*' \
  -H 'origin: https://www.youtube.com' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.youtube.com/embed/mGtFUm-sgh4' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: GPS=1; YSC=4S-NZ-lVQRY; VISITOR_INFO1_LIVE=NWxGPros3d4; PREF=f4=4000000&tz=America.New_York; CONSISTENCY=AGDxDePYXQ1vmLdjTyvtxbflwDptzVb6DNE7fe-ES5OkP2kpsuXkB7vasF0d_KJqWazDPpnT-vgV_nnemV20asnA7T0UuVwb6dzy6ceulKLKrTnax2lVZL9bj5v65AUTo-yPlVIeyvi-IDrhT-K0-as' \
  --data-raw '{"videoId":"mGtFUm-sgh4","context":{"client":{"hl":"en","gl":"US","remoteHost":"2620:0:2820:2221:2486:cc62:d30a:61db","deviceMake":"","deviceModel":"","visitorData":"CgtOV3hHUHJvczNkNCijjrSSBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36,gzip(gfe)","clientName":"WEB_EMBEDDED_PLAYER","clientVersion":"1.20220403.00.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/embed/mGtFUm-sgh4","screenPixelDensity":2,"platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CKOOtJIGELfLrQUQ1IOuBRDwgq4FENi-rQU%3D"},"screenDensityFloat":1.5,"timeZone":"America/New_York","browserName":"Chrome","browserVersion":"99.0.4844.84","screenWidthPoints":396,"screenHeightPoints":609,"utcOffsetMinutes":-240,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","connectionType":"CONN_CELLULAR_4G","playerType":"UNIPLAYER","tvAppInfo":{"livingRoomAppMode":"LIVING_ROOM_APP_MODE_UNSPECIFIED"},"clientScreen":"EMBED"},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"consistencyTokenJars":[{"encryptedTokenJarContents":"AGDxDePYXQ1vmLdjTyvtxbflwDptzVb6DNE7fe-ES5OkP2kpsuXkB7vasF0d_KJqWazDPpnT-vgV_nnemV20asnA7T0UuVwb6dzy6ceulKLKrTnax2lVZL9bj5v65AUTo-yPlVIeyvi-IDrhT-K0-as"}],"internalExperimentFlags":[]},"clientScreenNonce":"MC40MDYyNjA3MTY0OTEyMjA0","adSignalsInfo":{"params":[{"key":"dt","value":"1649215269608"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"-240"},{"key":"u_his","value":"3"},{"key":"u_h","value":"720"},{"key":"u_w","value":"1280"},{"key":"u_ah","value":"680"},{"key":"u_aw","value":"1280"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"609"},{"key":"biw","value":"396"},{"key":"brdim","value":"0,0,0,0,1280,0,1280,680,396,609"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"playbackContext":{"contentPlaybackContext":{"html5Preference":"HTML5_PREF_WANTS","lactMilliseconds":"15","referer":"https://www.youtube.com/embed/mGtFUm-sgh4","signatureTimestamp":19086,"autoCaptionsDefaultOn":false,"mdxContext":{},"playerWidthPixels":396,"playerHeightPixels":609,"ancestorOrigins":[]}},"cpn":"7Mwa31-yBWpsLnjV","captionParams":{},"serviceIntegrityDimensions":{"poToken":"GpsBCm6zuxDtAEXCjhWFr9xMVbMm2OMT-qQdfwybV1PmEHwKO5gPkyyPFWDmhlThEhDqiWZAro2EVXyAvoxphZByDr_DA-EDh-l4ziQLceofuiHaoqWUOLocjFmxA2JqwyWayy0KbBtGEx0tVAV76yNd-xIpATwYQQ6gjjYg93q1yruZvZqqDZ3lUJHXAc0fDPs4hJWTLqNm8Oq0sr8="}}' \
  --compressed > output.json