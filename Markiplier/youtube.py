import requests
import json

from Graph import *

class Crawler(Graph):
    def __init__(self, root_vid_id, root_vid_name, key):
        self.root_vid_name = root_vid_name
        self.root_vid_id = root_vid_id
        self.key = key
        self.graph = nx.MultiDiGraph()
        self.network = Network()
    
    def parse(self, videoId):
        link = "https://www.youtube.com/youtubei/v1/player?key=" + self.key + "W8&prettyPrint=true"
        headers = {
        'authority' : 'www.youtube.com',
        'sec-ch-ua' : '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-full-version-list' : '" Not A;Brand";v="99.0.0.0", "Chromium";v="99.0.4844.84", "Google Chrome";v="99.0.4844.84"',
        'content-type' : 'application/json',
        'sec-ch-ua-mobile' : '?0',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'sec-ch-ua-arch' : '"x86"',
        'sec-ch-ua-full-version' : '"99.0.4844.84"',
        'sec-ch-ua-platform-version' : '"10.0.0"',
        'x-youtube-client-name' : '56',
        'x-youtube-client-version' : '1.20220403.00.00',
        'sec-ch-ua-bitness' : '"64"',
        'sec-ch-ua-model' : '',
        'x-goog-visitor-id' : 'CgtOV3hHUHJvczNkNCijjrSSBg%3D%3D', 
        'sec-ch-ua-platform' : '"Windows"',
        'accept' : '/',
        'origin' : 'https://www.youtube.com/',
        'sec-fetch-site' : 'same-origin',
        'sec-fetch-mode' : 'cors',
        'sec-fetch-dest' : 'empty',
        'referer' : 'https://www.youtube.com/embed/' + videoId,
        'accept-language' : 'en-US,en;q=0.9',
        'cookie' : 'GPS=1; YSC=4S-NZ-lVQRY; VISITOR_INFO1_LIVE=NWxGPros3d4; PREF=f4=4000000&tz=America.New_York; CONSISTENCY=AGDxDePYXQ1vmLdjTyvtxbflwDptzVb6DNE7fe-ES5OkP2kpsuXkB7vasF0d_KJqWazDPpnT-vgV_nnemV20asnA7T0UuVwb6dzy6ceulKLKrTnax2lVZL9bj5v65AUTo-yPlVIeyvi-IDrhT-K0-as'
        }
        data = {"videoId":videoId,"context":{"client":{"hl":"en","gl":"US","remoteHost":"2620:0:2820:2221:2486:cc62:d30a:61db","deviceMake":"","deviceModel":"","visitorData":"CgtOV3hHUHJvczNkNCijjrSSBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36,gzip(gfe)","clientName":"WEB_EMBEDDED_PLAYER","clientVersion":"1.20220403.00.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/embed/mGtFUm-sgh4","screenPixelDensity":"2","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CKOOtJIGELfLrQUQ1IOuBRDwgq4FENi-rQU%3D"},"screenDensityFloat":"1.5","timeZone":"America/New_York","browserName":"Chrome","browserVersion":"99.0.4844.84","screenWidthPoints":"396","screenHeightPoints":"609","utcOffsetMinutes":"-240","userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","connectionType":"CONN_CELLULAR_4G","playerType":"UNIPLAYER","tvAppInfo":{"livingRoomAppMode":"LIVING_ROOM_APP_MODE_UNSPECIFIED"},"clientScreen":"EMBED"},"user":{"lockedSafetyMode":"false"},"request":{"useSsl":"true","consistencyTokenJars":[{"encryptedTokenJarContents":"AGDxDePYXQ1vmLdjTyvtxbflwDptzVb6DNE7fe-ES5OkP2kpsuXkB7vasF0d_KJqWazDPpnT-vgV_nnemV20asnA7T0UuVwb6dzy6ceulKLKrTnax2lVZL9bj5v65AUTo-yPlVIeyvi-IDrhT-K0-as"}],"internalExperimentFlags":[]},"clientScreenNonce":"MC40MDYyNjA3MTY0OTEyMjA0","adSignalsInfo":{"params":[{"key":"dt","value":"1649215269608"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"-240"},{"key":"u_his","value":"3"},{"key":"u_h","value":"720"},{"key":"u_w","value":"1280"},{"key":"u_ah","value":"680"},{"key":"u_aw","value":"1280"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"609"},{"key":"biw","value":"396"},{"key":"brdim","value":"0,0,0,0,1280,0,1280,680,396,609"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"playbackContext":{"contentPlaybackContext":{"html5Preference":"HTML5_PREF_WANTS","lactMilliseconds":"15","referer":"https://www.youtube.com/embed/mGtFUm-sgh4","signatureTimestamp":"19086","autoCaptionsDefaultOn":"false","mdxContext":{},"playerWidthPixels":"396","playerHeightPixels":"609","ancestorOrigins":[]}},"cpn":"7Mwa31-yBWpsLnjV","captionParams":{},"serviceIntegrityDimensions":{"poToken":"GpsBCm6zuxDtAEXCjhWFr9xMVbMm2OMT-qQdfwybV1PmEHwKO5gPkyyPFWDmhlThEhDqiWZAro2EVXyAvoxphZByDr_DA-EDh-l4ziQLceofuiHaoqWUOLocjFmxA2JqwyWayy0KbBtGEx0tVAV76yNd-xIpATwYQQ6gjjYg93q1yruZvZqqDZ3lUJHXAc0fDPs4hJWTLqNm8Oq0sr8="}}
    
        response = requests.post(link, headers=headers, json=data)

        player_data = response.text
        player_json = json.loads(player_data)
        if "endscreen" in player_json:
            items = player_json["endscreen"]["endscreenRenderer"]["elements"]
        else:
            return None
    
        nodes = []
        for item in items:
            node = {}
            node["name"] = item["endscreenElementRenderer"]["title"]["runs"][0]["text"]
            node["id"] = item["endscreenElementRenderer"]["endpoint"]["watchEndpoint"]["videoId"]
            nodes.append(node)


        return nodes
       
    # Method to relabel the network x nodes
    def relabel(self, nodes):
        names = dict()
        for node in nodes:
            print(node, flush=True)
            if node["name"] not in names:
                names[node["name"]] = []
            names[node["name"]].append(node)
        
        for name in names:
            if len(names[name]) == 1:
                continue
            for i in range(len(names[name])):
                names[name][i]["name"] += " ({0})".format(i+1)
        
        mapping = {}
        for node in nodes:
            mapping[node["id"]] = node["name"]
        self.graph = nx.relabel_nodes(self.graph, mapping)
    
    # Method to actually crawl the videos
    def crawl(self):
        # Initializing queue with root
        queue = [{
            "name": self.root_vid_name,
            "id": self.root_vid_id
            }]
        finished = []

        # Going till queue empty
        while (len(queue) > 0):
            parent = queue.pop(0)
            print(parent, flush=True)
            finished.append(parent)
            
            # Adding to pages and queue
            children = self.parse(parent["id"])
            
            if children is not None:
                for child in children:
                    print(child)
                    self.graph.add_edge(parent["id"], child["id"])
            
            if (children is None):
                continue
            for item in children:
                if item not in finished and item not in queue:
                    queue.append(item)
                '''
                if item[key] not in finished and item[key] not in queue:
                    queue.append(item[key])
                '''
        
        self.relabel(finished)
        
        return finished


def get_data(videoId, key):
    link = "https://www.youtube.com/youtubei/v1/player?key=" + key + "W8&prettyPrint=true"
    headers = {
    'authority' : 'www.youtube.com',
    'sec-ch-ua' : '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-full-version-list' : '" Not A;Brand";v="99.0.0.0", "Chromium";v="99.0.4844.84", "Google Chrome";v="99.0.4844.84"',
    'content-type' : 'application/json',
    'sec-ch-ua-mobile' : '?0',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'sec-ch-ua-arch' : '"x86"',
    'sec-ch-ua-full-version' : '"99.0.4844.84"',
    'sec-ch-ua-platform-version' : '"10.0.0"',
    'x-youtube-client-name' : '56',
    'x-youtube-client-version' : '1.20220403.00.00',
    'sec-ch-ua-bitness' : '"64"',
    'sec-ch-ua-model' : '',
    'x-goog-visitor-id' : 'CgtOV3hHUHJvczNkNCijjrSSBg%3D%3D', 
    'sec-ch-ua-platform' : '"Windows"',
    'accept' : '/',
    'origin' : 'https://www.youtube.com/',
    'sec-fetch-site' : 'same-origin',
    'sec-fetch-mode' : 'cors',
    'sec-fetch-dest' : 'empty',
    'referer' : 'https://www.youtube.com/embed/' + videoId,
    'accept-language' : 'en-US,en;q=0.9',
    'cookie' : 'GPS=1; YSC=4S-NZ-lVQRY; VISITOR_INFO1_LIVE=NWxGPros3d4; PREF=f4=4000000&tz=America.New_York; CONSISTENCY=AGDxDePYXQ1vmLdjTyvtxbflwDptzVb6DNE7fe-ES5OkP2kpsuXkB7vasF0d_KJqWazDPpnT-vgV_nnemV20asnA7T0UuVwb6dzy6ceulKLKrTnax2lVZL9bj5v65AUTo-yPlVIeyvi-IDrhT-K0-as'
    }
    data = {"videoId":videoId,"context":{"client":{"hl":"en","gl":"US","remoteHost":"2620:0:2820:2221:2486:cc62:d30a:61db","deviceMake":"","deviceModel":"","visitorData":"CgtOV3hHUHJvczNkNCijjrSSBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36,gzip(gfe)","clientName":"WEB_EMBEDDED_PLAYER","clientVersion":"1.20220403.00.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/embed/mGtFUm-sgh4","screenPixelDensity":"2","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CKOOtJIGELfLrQUQ1IOuBRDwgq4FENi-rQU%3D"},"screenDensityFloat":"1.5","timeZone":"America/New_York","browserName":"Chrome","browserVersion":"99.0.4844.84","screenWidthPoints":"396","screenHeightPoints":"609","utcOffsetMinutes":"-240","userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","connectionType":"CONN_CELLULAR_4G","playerType":"UNIPLAYER","tvAppInfo":{"livingRoomAppMode":"LIVING_ROOM_APP_MODE_UNSPECIFIED"},"clientScreen":"EMBED"},"user":{"lockedSafetyMode":"false"},"request":{"useSsl":"true","consistencyTokenJars":[{"encryptedTokenJarContents":"AGDxDePYXQ1vmLdjTyvtxbflwDptzVb6DNE7fe-ES5OkP2kpsuXkB7vasF0d_KJqWazDPpnT-vgV_nnemV20asnA7T0UuVwb6dzy6ceulKLKrTnax2lVZL9bj5v65AUTo-yPlVIeyvi-IDrhT-K0-as"}],"internalExperimentFlags":[]},"clientScreenNonce":"MC40MDYyNjA3MTY0OTEyMjA0","adSignalsInfo":{"params":[{"key":"dt","value":"1649215269608"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"-240"},{"key":"u_his","value":"3"},{"key":"u_h","value":"720"},{"key":"u_w","value":"1280"},{"key":"u_ah","value":"680"},{"key":"u_aw","value":"1280"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"609"},{"key":"biw","value":"396"},{"key":"brdim","value":"0,0,0,0,1280,0,1280,680,396,609"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"playbackContext":{"contentPlaybackContext":{"html5Preference":"HTML5_PREF_WANTS","lactMilliseconds":"15","referer":"https://www.youtube.com/embed/mGtFUm-sgh4","signatureTimestamp":"19086","autoCaptionsDefaultOn":"false","mdxContext":{},"playerWidthPixels":"396","playerHeightPixels":"609","ancestorOrigins":[]}},"cpn":"7Mwa31-yBWpsLnjV","captionParams":{},"serviceIntegrityDimensions":{"poToken":"GpsBCm6zuxDtAEXCjhWFr9xMVbMm2OMT-qQdfwybV1PmEHwKO5gPkyyPFWDmhlThEhDqiWZAro2EVXyAvoxphZByDr_DA-EDh-l4ziQLceofuiHaoqWUOLocjFmxA2JqwyWayy0KbBtGEx0tVAV76yNd-xIpATwYQQ6gjjYg93q1yruZvZqqDZ3lUJHXAc0fDPs4hJWTLqNm8Oq0sr8="}}

    response = requests.post(link, headers=headers, json=data)
    return response

if __name__ == "__main__":
    '''
    videoId = "mGtFUm-sgh4"
    key = "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qc"

    player_data = get_data(videoId, key).text
    player_json = json.loads(player_data)
    items = player_json["endscreen"]["endscreenRenderer"]["elements"]

    titles = []
    videoIds = []
    for item in items:
        titles.append(item["endscreenElementRenderer"]["title"]["runs"][0]["text"])
        for id in item["endscreenElementRenderer"]["endpoint"]["watchEndpoint"]:
            videoIds.append(item["endscreenElementRenderer"]["endpoint"]["watchEndpoint"][id])

    print(videoIds)
    print(titles)
    '''
    fandom = Crawler("j64oZLF443g", "Markiplier in Space Part 1", "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qc")
    fandom.parse("mGtFUm-sgh4")
    nodes = fandom.crawl()
    fandom.plot_pretty()
    print()
