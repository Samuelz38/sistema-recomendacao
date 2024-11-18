from deep_translator import GoogleTranslator

def translateText(text: str, source: str, target: str) -> str:

  translator = GoogleTranslator(source=source, target=target)

  return translator.translate(text)