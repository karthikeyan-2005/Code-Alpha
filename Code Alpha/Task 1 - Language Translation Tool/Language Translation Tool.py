import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        self.from_label = ttk.Label(root, text="From:")
        self.from_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.from_lang = ttk.Combobox(root, values=list(LANGUAGES.values()), width=20)
        self.from_lang.grid(row=0, column=1, padx=5, pady=5)
        self.from_lang.set("English")  # Default language is English
        
        self.to_label = ttk.Label(root, text="To:")
        self.to_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        self.to_lang = ttk.Combobox(root, values=list(LANGUAGES.values()), width=20)
        self.to_lang.grid(row=1, column=1, padx=5, pady=5)
        self.to_lang.set("Select Language")
        
        self.input_label = ttk.Label(root, text="Enter text to translate:")
        self.input_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        self.input_text = tk.Text(root, height=5, width=40)
        self.input_text.grid(row=2, column=1, padx=5, pady=5)
        
        self.output_label = ttk.Label(root, text="Translated Text:")
        self.output_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        
        self.output_text = tk.Text(root, height=5, width=40, state="disabled")
        self.output_text.grid(row=3, column=1, padx=5, pady=5)
        
        self.translate_button = ttk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=4, columnspan=2, padx=5, pady=5)
        
    def translate_text(self):
        translator = Translator()
        text = self.input_text.get("1.0", "end-1c")  # Get text from input_text widget
        from_lang = [key for key, value in LANGUAGES.items() if value == self.from_lang.get()][0]
        to_lang = [key for key, value in LANGUAGES.items() if value == self.to_lang.get()][0]

        translated = translator.translate(text, src=from_lang, dest=to_lang)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", translated.text)
        self.output_text.config(state="disabled")

# Language codes and their corresponding languages
LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'iw': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'rw': 'Kinyarwanda',
    'ko': 'Korean',
    'ku': 'Kurdish (Kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'or': 'Odia',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots Gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'ug': 'Uyghur',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu'
}

def main():
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
