# Gemini_API.py

import base64
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


from database import HealthRecord

load_dotenv()

def get_gemini_cardio_analysis(health_data: dict):

    # Gemini API'sine göndermek için prompt metni oluşturma
    # Verileri daha okunabilir bir formatta sunun
    prompt_text = f"""
     Bir hasta verisi gönderildi. Lütfen bu verilere dayanarak bir analiz yapın:
     - Yaş: {health_data.get('age', 'Belirtilmemiş')}
     - Cinsiyet: {health_data.get('gender', 'Belirtilmemiş')}
     - Kolesterol (LDL/HDL): {health_data.get('cholesterol_ldl', 'Belirtilmemiş')}/{health_data.get('cholesterol_hdl', 'Belirtilmemiş')}
     - Sigara kullanımı: {'Evet' if health_data.get('smoking') else 'Hayır'}
     - Kan basıncı: {health_data.get('blood_pressure', 'Belirtilmemiş')}
     - Ailede kalp hastalığı öyküsü: {'Evet' if health_data.get('family_history') else 'Hayır'}
     - Günlük aktivite seviyesi: {health_data.get('activity_level', 'Belirtilmemiş')}
     - Mevcut boy ve kilo: {health_data.get('height', 'Belirtilmemiş')} cm, {health_data.get('weight', 'Belirtilmemiş')} kg

     Bu veriler ışığında, kalp hastalığı riskini az, normal veya yüksek olarak sınıflandırın. Ardından, bu riskleri düşürmeye yönelik kişiselleştirilmiş ve uygulanabilir diyet önerileri sunun.
     """


    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt_text),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text="""Lütfen çok yetenekli kardiyovasküler uzmanı ve uzman bir diyetisyen gibi davran. Görevin, verilen verilerden kalp hastalığı riskini az, normal ve yüksek diye sınıflandırmak, sonrasında ise kalp hastalıkları riskini düşürmek için kişiselleştirilmiş diyet önerileri sunmak. Bu önerileri yaparken, sana sağlayacağım aşağıdaki verileri göz önünde bulundur:
            Kolesterol (LDL/HDL), Yaş, Cinsiyet, Sigara kullanımı, Kan basıncı, Ailede kalp hastalığı öyküsü, Günlük aktivite seviyesi, Mevcut boy ve kilo
            Bu verileri kullanarak, yüksek kolesterolü düşürmeye, kan basıncını dengelemeye ve genel kalp sağlığını iyileştirmeye odaklanan, detaylı ve uygulanabilir bir beslenme planı oluştur. Önerilerin bilimsel temellere dayalı ve açıklayıcı olsun."""),
        ],
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return response.text.replace('```', '')


if __name__ == "__main__":
    get_gemini_cardio_analysis()