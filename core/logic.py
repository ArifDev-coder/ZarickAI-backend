import json
import os
from .response import Respond

def get_bot_name():
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, "..", "data", "config.json")
    config_path = os.path.abspath(config_path)    
    
    with open(config_path, "r") as f:
        config = json.load(f)
    return config.get("bot_name", "AI")

class BotRespond:
    @staticmethod
    def hai(message):
        commandLst = [
            "hai", "hei", "hey", "oi", "whatsup", "hello", "halo", "woi",
            "yo", "hi", "hola", "assalamualaikum", "permisi", "haloo", "heii"
        ]
        return any(word in message.split() for word in commandLst)

    @staticmethod
    def motivasi(message):
        return any(word in message for word in ["motivasi", "semangatin", "butuh semangat", "inspirasi", "quotes"])

    @staticmethod
    def sedih(message):
        return any(word in message for word in ["sedih", "down", "lelah", "pusing", "bingung"])

    @staticmethod
    def semangat(message):
        return any(word in message for word in ["semangat", "ayo", "gas", "fight", "ayo semangat", "capek"])
    
    @staticmethod
    def kabar(message):
        return any(word in message for word in ["apa kabar", "gimana kabarnya", "kabarmu", "kabar kamu"])

    @staticmethod
    def cuaca(message):
        return any(word in message for word in ["cuaca", "panas", "dingin", "mendung", "hujan"])

    @staticmethod
    def ngapain(message):
        return any(word in message for word in ["lagi apa", "ngapain", "lagi sibuk?", "lagi ngapain?"])

    @staticmethod
    def makasih(message):
        return any(word in message for word in ["makasih", "terima kasih", "thanks", "thx"])


def get_bot_response(message):
    message = message.lower()

    if BotRespond.hai(message):
        return Respond.hai()
    
    elif BotRespond.motivasi(message):
        return Respond.motivasi()
    
    elif BotRespond.sedih(message):
        return Respond.sedih()
    
    elif BotRespond.semangat(message):
        return Respond.semangat()
    
    elif BotRespond.kabar(message):
        return Respond.kabar()
    
    elif BotRespond.cuaca(message):
        return Respond.cuaca()
    
    elif BotRespond.ngapain(message):
        return Respond.ngapain()
    
    elif BotRespond.makasih(message):
        return Respond.makasih()

    elif "test" in message:
        return (
            "Ini adalah pesan test yang lumayan panjang. 👋\n\n"
            "Saya adalah chatbot yang sedang dalam pengembangan. "
            "Saat ini saya bisa merespons beberapa kata kunci seperti:\n"
            "- Sapaan (hai, hello, halo)\n"
            "- Motivasi dan semangat\n"
            "- Pertanyaan kabar\n"
            "- Cuaca\n"
            "- Dan beberapa hal lainnya\n\n"
            "Silakan coba berbicara dengan saya menggunakan kata-kata tersebut! 😊"
        )

    else:
        return "Aku belum ngerti maksudmu 😅."