# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

import json
import typing


class CryptoMacroSentinel(gl.Contract):
    has_scanned: bool
    risk_score: str
    btc_bias: str
    analysis: str
    data_url: str

    def __init__(self, data_url: str):
        self.has_scanned = False
        self.risk_score = "50"
        self.btc_bias = "NEUTRAL"
        self.analysis = "Awaiting first scan"
        self.data_url = data_url

    @gl.public.write
    def scan_macro(self) -> typing.Any:

        if self.has_scanned:
            return "Already scanned"

        def nondet() -> str:
            response = gl.nondet.web.get(self.data_url)
            fng = response.body.decode("utf-8")
            print(fng)

            task = f"""You are a macro analyst for crypto markets.
            Here is Fear and Greed Index data:
            {fng}

            Rate the current macro risk environment for Bitcoin.

            Respond with the following JSON format:
            {{
                "risk_score": str,
                "btc_bias": str,
                "summary": str
            }}
            risk_score: a number from 0 to 100 as a string, where 0 means extreme fear, 100 means extreme greed.
            btc_bias: must be one of STRONG_BEAR, BEAR, NEUTRAL, BULL, STRONG_BULL.
            summary: one sentence macro analysis.
            It is mandatory that you respond only using the JSON format above,
            nothing else. Don't include any other words or characters,
            your output must be only JSON without any formatting prefix or suffix.
            This result should be perfectly parsable by a JSON parser without errors.
            """
            result = gl.nondet.exec_prompt(task).replace("```json", "").replace("```", "")
            print(result)
            return json.dumps(json.loads(result), sort_keys=True)

        result_json = json.loads(gl.eq_principle.strict_eq(nondet))

        self.has_scanned = True
        self.risk_score = str(result_json["risk_score"])
        self.btc_bias = result_json["btc_bias"]
        self.analysis = result_json["summary"]

        return result_json
