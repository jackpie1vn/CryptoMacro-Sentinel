# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

import json
import typing


class CryptoMacroSentinel(gl.Contract):
    has_scanned: bool
    risk_score: str
    btc_bias: str
    analysis: str
    param: str

    def __init__(self, param: str):
        self.has_scanned = False
        self.risk_score = "50"
        self.btc_bias = "NEUTRAL"
        self.analysis = "Awaiting scan"
        self.param = param

    @gl.public.write
    def scan_macro(self) -> typing.Any:

        if self.has_scanned:
            return "Already scanned"

        def nondet() -> str:
            fng = gl.nondet.web.render("https://alternative.me/crypto/fear-and-greed-index/", mode="text")
            print(fng)

            task = f"""You are a macro risk analyst for crypto markets.
            Here is current crypto market data:
            {fng[:1500]}

            Rate the current macro risk environment for Bitcoin.

            Respond with the following JSON format:
            {{
                "risk_score": str,
                "btc_bias": str,
                "summary": str
            }}
            risk_score: 0-100 as string, 0 means extreme fear, 100 means extreme greed.
            btc_bias: one of STRONG_BEAR, BEAR, NEUTRAL, BULL, STRONG_BULL.
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
