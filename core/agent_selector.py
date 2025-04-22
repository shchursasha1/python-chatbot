class AgentSelector:
    def __init__(self, agents):
        self.agents = agents
        self.last_agent = None

    def select_agent(self, user_input):
        lowered = user_input.lower()
        if "@sentinel" in lowered:
            agent = self.agents['sentinel']
        elif "@finguide" in lowered:
            agent = self.agents['finguide']
        elif "@edubot" in lowered:
            agent = self.agents['edubot']
        else:
            # Professional: Advanced heuristic for agent selection
            security_words = [
                "protect", "secure", "phishing", "password", "cyber", "safety", "hack", "breach", "fraud",
                "attack", "malware", "scam", "theft", "privacy", "compromise"
            ]
            finance_words = [
                "budget", "finance", "cost", "expense", "money", "investment", "invest", "loan", "credit", "debt",
                "tax", "income", "salary", "purchase", "price", "spend", "save", "saving", "fund", "bank", "profit",
                "loss", "account", "insurance", "mortgage", "dividend", "stock", "bond", "asset", "liability",
                "capital", "payment", "bill", "wealth", "economics", "economic", "financial", "card", "statement", "transaction", "transfer"
            ]
            # Якщо є security-слово + фінансовий об'єкт — це security-кейс (Sentinel)
            has_security = any(word in lowered for word in security_words)
            has_finance = any(word in lowered for word in finance_words)
            # Додатково: якщо є security-слово і фінансовий тригер в одному питанні
            finance_triggers = ["account", "bank", "finance", "credit", "card", "statement", "payment", "transaction", "transfer"]
            has_finance_trigger = any(word in lowered for word in finance_triggers)
            if has_security and has_finance_trigger:
                agent = self.agents['sentinel']
            elif has_security:
                agent = self.agents['sentinel']
            elif has_finance:
                agent = self.agents['finguide']
            elif any(word in lowered for word in ["explain", "teach", "learn"]):
                agent = self.agents['edubot']
            else:
                agent = self.last_agent or self.agents['edubot']
        switched = agent != self.last_agent
        self.last_agent = agent
        return agent, switched
