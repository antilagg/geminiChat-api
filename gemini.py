from curl_cffi import requests
import re
from flask import Flask, request, jsonify


class gemini:
    def __init__(self):
        self.session = requests.Session(impersonate="chrome124", verify=False)

    def main(self, prompt):
        headers = {
            'accept': '*/*',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://gemini.google.com',
            'referer': 'https://gemini.google.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'x-client-data': 'CIu2yQEIprbJAQipncoBCMToygEIlqHLAQiSo8sBCIWgzQEIyNHOAQju5s4BCLznzgEYrujOAQ==',
            'x-goog-ext-525001261-jspb': '[1,null,null,null,"f299729663a2343f"]',
            'x-same-domain': '1',
        }

        params = {
            'bl': 'boq_assistant-bard-web-server_20250413.12_p0',
            'f.sid': '-2432192671706889519',
            'hl': 'tr',
            '_reqid': '1357029',
            'rt': 'c',
        }

        data = 'f.req=%5Bnull%2C%22%5B%5B%5C%22'+prompt+'%5C%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C0%5D%2C%5B%5C%22tr%5C%22%5D%2C%5B%5C%22%5C%22%2C%5C%22%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22%5C%22%5D%2C%5C%22!g4ClgNjNAAYKOoS0KjpCpLfbsWUXtBA7ADQBEArZ1AbF8hwYKw-w5TFrUQVbh67ZxfAZ9GRFcx-OJXjHcTGjmqR-2OWsDYVkVzNjA5vwAgAAAEtSAAAABGgBB34AQR5TsPrzP-tg-jb0W-mmycbNudCUoA28W56WoxP0cC8vATtRSNQUx9R6uD1m5s4Lj0qilBgsogEzU_hhRA1xF0lGmQNOdiIOgsdFzKjCccxsMrbiceHU_AnUssmbm3YC37XG4RMQmJP67jTkzXWgbOrqkXqs_HxX-0na91X4TXMPoseLcTtHVB637sf59VN9Hm0dbYlbFST7iTjTnhk4-g2oT2ZFP_6PyHoODceqDD1gH2ZcW1vQCybblv4wyi_xxubynnU5fkaPwqK2NlOOp3anPy3AQCgerM9kioHc9eXO5YIVOVGczpJUK4IFErYzsBycUj1HQTxO43X1Cl1Z81h1cFv7lT5-seX-7QjFQ8ASbYvE3U8hOcxuB-TOKnTXml-chH8OUNlRMagOof7UMQ75tv8xxlsjkGZKTK2qg2ZypZlaWhJ_z1B8D0djsK1Y9NQGVstnCI0g52cP7s_Y3VkkG2MAU1mclbOcoc6NXov05N2T1kFFv1sC-vE1rEOg1I6H8qgH7JAIxPVpJRFHIhOGAEyjrq5nLhNdlYg6rGFIinD4PHgOfMbLe1o9WLVkeetDIpsvyPuJlFheonM5y7oQtkUKzVWvliSfebuMFN_l4M9rgAsmszKBgQvwIdAfylA1feFmLfmNSq6A-7Khu83seLCJaLq6xZdC3DBoc74JkUitd4-8m6Zp7WpFgi172aidNoubM1kfXb6lL-_nG7rzyclobR-v84xbq0Czl5Ms6XA5_SHddxXrzc4Amar2F-89eEGf30wdEWZqe7LFQNkV2Wwhx10I2Ey17yCT_TPg-qumgi3qDqiA8-Tu4_BlLlg6KFCFLUAGptVzrvbFch-y641LIckIbznpNpeTensrC9jtjASCvJyS8f2Am6uBBDBOcUQkGgnUWURZVRzQ1tJRbIBnz5jOiLWZJym8CDXVQ7TXHSv1yVrBq79_X1z1cwNZduTVjTp69g2N_FerlsXO9ezwfhjjMi5kbouwPawZMHL1k-nsSGxsqh9my3ZoU6jD_5RRyLKeTmy8aLOygcrn007B41nBA2RezyvmzBOMDss8N3kGy9M7stOULKv5NVxbu4VUeHd77YRnmvjpPgTExMvWJQNbDlg06Kpfx6DHfD_h3lhvciQsEGGt0GXQYQ9atmh0rrP2aQrSPPJnZRVQ1o9C6Ic42yiEfO08Mgb0MnkFukRscitL62estuSlS81Y%5C%22%2C%5C%22a9e0ea27f6d9f17469321cec78cb7f76%5C%22%2Cnull%2C%5B1%5D%2C1%2Cnull%2Cnull%2C1%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B0%5D%5D%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B2%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%22%5D&'

        res = self.session.post('https://gemini.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate',
        params=params,
        headers=headers,
        data=data)


        # ultra plus negro debugging 👌
        with open('debug_response.txt', 'w', encoding='utf-8') as f:
            f.write(res.text)

        _L = res.text.strip().split('\n')

        if _L and _L[0] == ")]}'":
            _L = _L[1:]

        _L = [l for l in _L if not l.strip().isdigit()]

        __res = []

        for _x in _L:
            if len(_x) < 20: continue
            try:
                _fnd = re.findall(r'"([^"]{20,})"', _x)
                for __m in _fnd:
                    if not any(j in __m for j in ['wrb.fr', 'rc_', 'null', 'true', 'false']):
                        if len(__m) > 20 and ' ' in __m:
                            __res.append(__m)
            except: pass

        if __res:
            __res.sort(key=len, reverse=True)
            _c = __res[0]
            for __x in __res[1:]:
                if not any(__x in _c for __x in [__x, __x.strip()]):
                    if __x.startswith((' (', '* ', '**')):
                        _c += ' ' + __x
            return self.__cleanup(_c)

        ___raw = res.text
        __matchy = re.findall(r'"([^"]{50,})"', ___raw)

        if __matchy:
            _valid = [v for v in __matchy if ' ' in v and len(v) > 100]
            if _valid:
                return self.__cleanup(max(_valid, key=len))

        return "not found"

    def __cleanup(self, __txt):
        if not __txt: return "not found"
        __txt = __txt.replace('\\n', '\n')
        __txt = re.sub(r'\\\s*\n', '\n', __txt)
        __txt = re.sub(r'\\$', '', __txt)
        __txt = __txt.replace('\\\\', '\\').replace('\\"', '"')
        return __txt.strip()


app = Flask(__name__)

@app.route('/api/gemini', methods=['POST'])
def handle_this_mess():
    try:
        payload = request.get_json()

        if not payload or 'prompt' not in payload:
            return jsonify({'err': 'congrats you sent nothing'}), 400

        whatever_you_wrote = payload['prompt']

        tryhard_ai = gemini()
        cursed_response = tryhard_ai.main(whatever_you_wrote)

        return jsonify({'deepthoughts': cursed_response})
    except Exception as meltdown:
        return jsonify({'wtf': str(meltdown)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
