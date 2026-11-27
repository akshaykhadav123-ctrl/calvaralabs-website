"""Hindi pages for calvaralabs.com (/hi/). Called from build.py as hindi.build(module).

Written for Indian buyers: plain Hindi, keeping trade words people use every day
(ग्रेड, CoA, सिलिका, मेश, पैलेट, बैग). Facts match the English pages.
"""

UI = {"wa": "व्हाट्सऐप पर अक्षय से बात करें", "top": "ऊपर", "top_label": "पेज के ऊपर जाएँ", "quote": "भाव", "quote_label": "भाव के फ़ॉर्म पर जाएँ"}

TICKER_HI = [
    ("मुफ़्त सैंपल", "किसी भी ग्रेड का सैंपल, उसके सर्टिफ़िकेट ऑफ़ एनालिसिस (CoA) के साथ।", "hi/contact", "अभी माँगें"),
    ("तैयार स्टॉक", "चार ग्रेड, 80 से 92 % Ca(OH)₂, 25, 30, 35 या 40 किलो के बैग में।", "hi/hydrated-lime", "ग्रेड देखें"),
    ("डिलीवरी", "जोधपुर प्लांट से या आपकी साइट तक, पैलेट पर या बिना पैलेट।", "hi/contact", "भाव पूछें"),
    ("नया", "हाइड्रॉक्सीएपेटाइट माइक्रो ग्रेड: 250 ग्राम के सैंपल उपलब्ध।", "hydroxyapatite", "जानें"),
]
TICKER_HI_EXTRA = ["900 किलो के जंबो बैग", "सीधे इंजीनियर से बात करें"]

NAV_HI = [("hi/hydrated-lime", "हाइड्रेटेड लाइम"), ("hydroxyapatite", "हाइड्रॉक्सीएपेटाइट"), ("documents", "दस्तावेज़"),
          ("export", "भाव और एक्सपोर्ट"), ("hi/contact", "संपर्क")]

IND_HI = {
    "Water and wastewater": ("पानी और अपशिष्ट जल", "pH सुधार, पानी को नरम करना, भारी धातु और फ़ॉस्फ़ेट हटाना"),
    "Chemicals": ("केमिकल", "कैल्शियम लवण, ब्लीचिंग पाउडर, कास्टिक सोडा उत्पादन"),
    "Sugar industry": ("चीनी उद्योग", "गन्ने के रस की सफ़ाई और शोधन"),
    "Ceramics and glass": ("सिरेमिक और काँच", "कच्चा माल और प्रोसेस एडिटिव"),
    "Flue gas treatment": ("फ़्लू गैस ट्रीटमेंट", "SO<sub>2</sub> और HCl की स्क्रबिंग और न्यूट्रलाइज़ेशन"),
    "Construction": ("निर्माण", "चूने का प्लास्टर, मसाला, पुट्टी, मिट्टी स्थिरीकरण, AAC ब्लॉक"),
    "Steel and metallurgy": ("स्टील और धातु उद्योग", "फ़्लक्स, स्लैग कंडीशनिंग, एसिड न्यूट्रलाइज़ेशन"),
    "Paper, leather and textile": ("कागज़, चमड़ा और कपड़ा", "कॉस्टिसाइज़िंग, चमड़े से बाल हटाना, रंगाई और फ़िनिशिंग"),
    "Agriculture": ("कृषि", "मिट्टी का pH सुधार, खाद तैयार करना"),
}

# Hindi copy for the /hi/industries/<slug>/ pages (mirrors IND_CONTENT in build.py).
# en_name is used only to look up the industry icon; the rest is page copy.
IND_HI_CONTENT = {
    "water-treatment": {
        "en_name": "Water and wastewater", "h1": "पानी के ट्रीटमेंट के लिए हाइड्रेटेड लाइम",
        "lede": "पीने के पानी और प्रोसेस पानी में pH सुधार, सॉफ्टनिंग और हार्डनेस कंट्रोल। आपका सही ग्रेड वह है जो आपके पानी में सबसे कम अवशेष छोड़े।",
        "why": [
            "पानी में आप शुद्धता के लिए पैसा देते हैं, सिर्फ़ अल्कलाइनिटी के लिए नहीं। 92 ग्रेड में हमारे सारे ग्रेडों में से सबसे कम सिलिका और इनर्ट मैटर होती है, इसलिए डोज़िंग लाइन में कम अवशेष जमा होता है और पीछे कम स्लज बनता है।",
            "डोज़िंग के लिए महीनता ज़रूरी है: 92 ग्रेड का 98.5 % 200 मेश से पार होता है, जो पानी के प्लांट की कम मात्रा की डोज़िंग में सहजता से मिलकर घुल जाता है।",
            "कम बजट पर चलने वाले प्लांट सॉफ्टनिंग के लिए 90 ग्रेड पर जा सकते हैं, जहाँ थोड़ी ज़्यादा इनर्ट मैटर सहनीय हो। अपनी प्रक्रिया बताइए; हम सैंपल से पुष्टि करके तय करेंगे।"],
        "use": [
            "हाइड्रेटेड लाइम को स्लरी या सूखे पाउडर के रूप में डोज़ किया जाता है ताकि pH बढ़े, पानी सॉफ़्ट हो (लाइम-सोडा प्रोसेस) और नलकड़ी के ख़िलाफ़ कंडीशन हो। महीन, एक जैसा पाउडर डोज़िंग पंप और फ़ीडर को स्थिर रखता है।",
            "हम आपकी डोज़िंग विधि के अनुसार ग्रेड सप्लाई करते हैं, हर लॉट के साथ CoA, ताकि आपके पानी की गुणवत्ता के रिकॉर्ड हर डिलीवरी को संदर्भित कर सकें।"],
    },
    "effluent-treatment": {
        "en_name": "Water and wastewater", "h1": "एफ़्लुएंट ट्रीटमेंट के लिए हाइड्रेटेड लाइम",
        "lede": "ETP, CETP और ऑन-साइट प्लांट में pH न्यूट्रलाइज़ेशन, भारी धातुओं और फ़ॉस्फेट का अवक्षेपण। आमतौर पर पीने के पानी की शुद्धता से एक कदम नीचे, और कीमत में भी एक कदम नीचे।",
        "why": [
            "अवक्षेपण के काम के लिए 90 ग्रेड आमतौर पर शुरूआती बिंदु है: उतनी शुद्धता कि आपकी मेटल हाइड्रॉक्साइड और फ़ॉस्फेट साफ़ बहे, पर पीने के पानी जितनी अतिरिक्त महीनता का ख़र्च न हो।",
            "जहाँ ETP बड़ी मात्रा में चले और टन प्रति कीमत तय करे, वहाँ 85 ग्रेड स्टैंडर्ड रेंज का जवाब है। यह pH सुधार और बल्क अवक्षेपण वैसे ही करता है; हम ग्रेड को आपकी इनफ़्लुएंट से मिलाते हैं, लेबल से नहीं।",
            "अपने pH लक्ष्य और क्या आप अवक्षेपित कर रहे हैं, यह बताइए; अक्षय ग्रेड और उसके CoA के साथ सैंपल सुझाएँगे, ताकि पहले आप अपने प्लांट में जाँच कर सकें।"],
        "use": [
            "एफ़्लुएंट प्लांट में लाइम ख़ट्टी धाराएँ न्यूट्रलाइज़ करता है, भारी धातुओं को हाइड्रॉक्साइड के रूप में अवक्षेपित करता है और बायोलॉजिकल ट्रीटमेंट में फ़ॉस्फेट को सह-अवक्षेपित करता है। इसे रिएक्शन टैंक में डोज़ किया जाता है या लाइम-सोडा सॉफ्टनिंग का हिस्सा बनता है।",
            "पानी ट्रीटमेंट की तुलना में यहाँ डोज़िंग ज़्यादा होती है, इसलिए ज़्यादातर ETP ख़रीदार 25 से 40 किलो के बैग या 900 किलो के जंबो बैग लेते हैं, और लॉट-दर-लॉट समान महीनता को सबसे ऊँचे ग्रेड से ज़्यादा महत्व देते हैं।"],
    },
    "sugar": {
        "en_name": "Sugar industry", "h1": "चीनी के लिए हाइड्रेटेड लाइम",
        "lede": "गन्ने के रस और बीट लिकर की क्लीरिफिकेशन और शोधन: pH कंट्रोल, अशुद्धियों का अवक्षेपण और रंग की सुरक्षा, कुचलने के सीज़न के हर दिन।",
        "why": [
            "चीनी के मिल आमतौर पर 90 ग्रेड से शुरू होते हैं: यह सामान्य खुराक में कम अवशेष से रस साफ़ करता है, और पीने के पानी के 92 से सस्ता है, बिना उस अतिरिक्त महीनता की जो मिल को ज़रूर नहीं।",
            "ऊँची क्लैरिटी स्पेक या कंटिन्यूअस प्यूरिफिकेशन प्लांट चलाने वाले मिल 92 ग्रेड पर जा सकते हैं; उसकी कम सिलिका रस में अघुलनशील गिट्टी को बाहर रखती है।",
            "कुचलने का सीज़न सप्लाई का सबसे ज़रूरी समय है: सीज़न शुरू होने से पहले अपनी मात्रा हमारे साथ तय कर लें, और हर लॉट अपने CoA के साथ जाता है, ताकि मिल लैब पावर पर पुष्टि कर सके।"],
        "use": [
            "लाइम रस में डोज़ किया जाता है ताकि pH बढ़े, जहाँ यह अशुद्धियों, मोम और रंग-पदार्थों को जकड़कर उन्हें बाहर गिरा देता है। शोधन चरण में यह राख हटाने में भी मदद करता है और प्रोसेस को स्थिर रखता है।",
            "मिल इसे मिल्क-ऑफ़-लाइम स्लरी के रूप में या सीधे महीन पाउडर के रूप में डोज़ करते हैं। एक जैसी महीनता मिल्क को समान और क्लीरिफिकेशन को स्थिर रखती है।"],
    },
    "chemicals": {
        "en_name": "Chemicals", "h1": "केमिकल बनाने के लिए हाइड्रेटेड लाइम",
        "lede": "रीएजेंट और प्रोसेस सामग्री के रूप में: कैल्शियम लवण, ब्लीचिंग पाउडर, कास्टिक सोडा और अन्य कैल्शियम-आधारित केमिस्ट्री। यहाँ ग्रेड आपकी उत्पाद गुणवत्ता का हिस्सा है।",
        "why": [
            "केमिकल ख़रीदार 92 ग्रेड से शुरू करते हैं: रेंज की सबसे कम सिलिका इनर्ट मैटर को आपकी प्रतिक्रिया और तैयार उत्पाद से बाहर रखती है, और 200 मेश से 98.5 % की महीनता रीएजेंट को एक जैसा व्यवहार करती है।",
            "लाइम-सोडा तरीके से कास्टिक सोडा के लिए, लाइम सोडा आश के साथ मिलकर कास्टिक सोडा और कैल्शियम कार्बोनेट की कीचड़ बनाता है; वही शुद्धता की सोच लागू होती है। जहाँ केमिस्ट्री संवेदनशील है, अपनी स्पेक या मानक बताइए और हम सैंपल से पहले पुष्टि करेंगे कि कौन सा ग्रेड उसे पूरा करता है।"],
        "use": [
            "हाइड्रेटेड लाइम कैल्शियम लवण बनाने में सीधा रीएजेंट, ब्लीचिंग पाउडर उत्पादन में रीएजेंट, और सोडा-लाइम प्रोसेस के कास्टिसाइज़िंग चरण में काम करता है।",
            "अपनी इनकमिंग स्पेसिफिकेशन भेजिए, हम बताएँगे कौन सा ग्रेड उसे पूरा करता है। हर लॉट अपने CoA के साथ जाता है, जो आपकी क्वालिटी टीम पावर पर जाँच कर सकती है।"],
    },
    "ceramics-glass": {
        "en_name": "Ceramics and glass", "h1": "सिरामिक और काँच के लिए हाइड्रेटेड लाइम",
        "lede": "सिरामिक बॉडी, ग्लेज़ और काँच के बैच में रॉ सामग्री और प्रोसेस एडिटिव के रूप में, जहाँ कम इंप्योरिटी और बराबर महीनता बैच केमिस्ट्री को स्थिर रखती है।",
        "why": [
            "सिरामिक और काँच के ख़रीदार 92 ग्रेड पर चलते हैं क्योंकि बैच केमिस्ट्री बचाना उनका काम है: हमारी रेंज की सबसे कम सिलिका सीमा और सबसे ज़्यादा महीनता का मतलब है जो लाइम आप जोड़ रहे हैं, वही कर रही है जो आपने तय किया, और कुछ और नहीं।",
            "90 ग्रेड उन बैचों के लिए काम करता है जहाँ थोड़ी ज़्यादा इनर्ट फ़्राक्शन सहनीय हो; आप सप्लायर बदलने से पहले हम आपकी रॉ-सामग्री स्पेसिफिकेशन और सैंपल से पुष्टि करेंगे।"],
        "use": [
            "सिरामिक में हाइड्रेटेड लाइम बॉडी में फ़्लक्स और प्लास्टिसाइज़र के रूप में और ग्लेज़ में एडिटिव के रूप में काम करती है। काँच में यह बैच में कैल्शियम ऑक्साइड का स्रोत बनता है, जिससे काँच पानी में और मज़बूत और टिकाऊ होता है।",
            "बैच टन में वज़न होते हैं और धीरे से तैयार होते हैं, इसलिए ज़्यादातर सिरामिक और काँच के प्लांट ऐसे सप्लायर की क़द्र करते हैं जो एक ग्रेड को लगातार बनाए रखे; हमारा हर लॉट अपने CoA के साथ जाता है जिसमें मापा गया रिज़ल्ट लिखा होता है।"],
    },
    "flue-gas": {
        "en_name": "Flue gas treatment", "h1": "फ़्लू गैस ट्रीटमेंट के लिए हाइड्रेटेड लाइम",
        "lede": "ठोस ईंधन, वेस्ट-टू-एनर्जी और प्रोसेस वेंट्स के फ़्लू गैस स्कबर में SO₂ और HCl की स्क्रबिंग और न्यूट्रलाइज़ेशन। डोज़िंग भारी होती है, इसलिए ग्रेड एक कीमत का फैसला है।",
        "why": [
            "स्क्रबिंग एक मात्रा का खेल है: आप ज़्यादा गैस के ख़िलाफ़ ज़्यादा लाइम डोज़ करते हैं, इसलिए 85 ग्रेड आमतौर पर शुरूआती बिंदु है और कीमत-संवेदनशील लाइनों के लिए 80। कम ग्रेड में बस ज़्यादा इनर्ट मैटर होती है, इसलिए थोड़ा ज़्यादा डोज़ करना पड़ता है; ग्रेड नंबर आमतौर पर आपकी टन प्रति कीमत तय करता है।",
            "महीनता फिर भी मदद करती है: महीन पाउडर जल्दी न्यूट्रलाइज़ करता है और स्कबर स्लरी में अधजमी गिट्टी कम छोड़ता है। अगर आपका स्कबर तंग चलता है, एक ग्रेड ऊपर जाएँ और हमने दोनों का CoA दिखाकर तय करने देंगे।",
            "गैस की संरचना और स्कबर का प्रकार अक्षय को बताइए; वह ग्रेड और पैकिंग सुझाएँगे जिससे आपकी लैंड कीमत कम रहे।"],
        "use": [
            "हाइड्रेटेड लाइम की स्लरी ख़ट्टी गैस स्क्रबिंग का मानक एब्ज़ॉर्बेंट है: यह SO₂ और HCl को न्यूट्रलाइज़ करके स्थिर कैल्शियम लवण में बदलता है जो स्कबर के कचरे के साथ बाहर निकलते हैं।",
            "प्लांट बड़े डे-टैंक से डोज़ करते हैं, इसलिए ज़्यादातर फ़्लू-गैस ख़रीदार 900 किलो के जंबो बैग लेते हैं, और उस स्थिर, सूखे पाउडर की क़द्र करते हैं जो बिना लम्प के स्लरी बन जाए।"],
    },
    "construction": {
        "en_name": "Construction", "h1": "निर्माण के लिए हाइड्रेटेड लाइम",
        "lede": "प्लास्टर, मसाला, लाइम पटी, मिट्टी स्थिरीकरण और AAC ब्लॉक: चूने के कारोबार की रोज़मर्रा की, किफ़ायती तरफ़, जहाँ 80 ग्रेड काम करता है।",
        "why": [
            "निर्माण काम बल्क में होता है, इसलिए 80 ग्रेड सही है: 80 % न्यूनतम Ca(OH)₂, हमारी रेंज में सबसे कम कीमत पर, नमी 2.0 % या उससे कम, ताकि मसाले और स्थिरीकरण के मिश्रण में साफ़ मिले।",
            "AAC ब्लॉक और पटी के लिए, जहाँ महीनता और प्रतिक्रियाशीलता उत्पाद में दिखती है, 85 ग्रेड आम कदम ऊपर है। हम आपके मिक्स डिज़ाइन से पुष्टि करके सौदा तय करेंगे।"],
        "use": [
            "प्लास्टर और मसाले में हाइड्रेटेड लाइम कामदारी और फ़िनिश बढ़ाता है। मिट्टी स्थिरीकरण में यह सड़क और फ़ाउंडेशन की ज़्यादा-प्लास्टिसिटी वाली कच्ची मिट्टी को सूखा और मज़बूत करता है। AAC ब्लॉक में यह कैल्शियम का स्रोत है जो ऑटोकलेव में फ़्लाई ऐश या सिलिका के साथ मिलकर कैल्शियम सिलिकेट हाइड्रेट बनाता है, जो ब्लॉक को मज़बूती देता है।",
            "बिल्डर और ब्लॉक प्लांट आमतौर पर 25 से 40 किलो के बैग पैलेट पर या बिना पैलेट लेते हैं, और इन्हें सूखे, ज़मीन से ऊँचे और ढक्कन के नीचे रखते हैं।"],
    },
    "steel": {
        "en_name": "Steel and metallurgy", "h1": "स्टील और धातु के लिए हाइड्रेटेड लाइम",
        "lede": "स्टील और गैर-लेहस पादु शॉप में फ़्लक्स, स्लैग कंडीशनिंग और एसिड न्यूट्रलाइज़ेशन, जहाँ ग्रेड कीमत और आपकी स्लैग केमिस्ट्री पर तय होता है।",
        "why": [
            "स्टील प्लांट बल्क फ़्लक्स और न्यूट्रलाइज़ेशन के काम में आमतौर पर 80 ग्रेड से शुरू होते हैं: अल्कलाइनिटी ही प्रोसेस काम में लेता है, और टन प्रति कीमत ही वह है जिसके ख़िलाफ़ प्रोसेस कीमत पर होता है।",
            "जहाँ स्लैग या डस्ट ट्रीटमेंट की इंप्योरिटी सीमा तंग हो, वहाँ 85 ग्रेड आम कदम ऊपर है। लाइम आपकी प्रक्रिया में कौन सी जगह लेता है यह बताइए और हम ग्रेड और उससे जाँचने का सैंपल सुझाएँगे।"],
        "use": [
            "धातु के प्लांट में हाइड्रेटेड लाइम ख़ट्टा पिकलिंग एसिड और ख़ट्टी ऑफ़-गैस न्यूट्रलाइज़ करता है, प्लांट एफ़्लुएंट का इलाज करता है, और ड्रायिंग वायर में कोटिंग वाहक के रूप में काम आता है। फ़्लक्स के रूप में इस्तेमाल होने पर यह उस स्लैग के बनने में मदद करता है जो सल्फ़र और फ़ॉस्फ़रस को पिघली धातु से बाहर ले जाता है।",
            "ज़्यादातर धातु के शॉप इसे बल्क डोज़िंग के लिए जंबो बैग में, या छोटी लाइनों के लिए 40 किलो के बैग में लेते हैं, और हर डिलीवरी को हमारे साथ भेजे CoA के ख़िलाफ़ जाँचते हैं।"],
    },
    "paper-leather": {
        "en_name": "Paper, leather and textile", "h1": "काग़ज़, चमड़े और कपड़ों के लिए हाइड्रेटेड लाइम",
        "lede": "कास्टिसाइज़िंग, चमड़े से बाल हटाना, और कपड़े के प्लांट की रंगाई और फ़िनिशिंग की नहानियाँ: रोज़ चलने वाली प्रक्रिया में स्थिर, महीन लाइम।",
        "why": [
            "यहाँ 85 ग्रेड आम पसंद है: कास्टिसाइज़िंग के लिए पर्याप्त महीन, स्टैंडर्ड रेंज में कीमत, और बच-दर-बच स्थिर — यह ज़रूरी है जब आपकी वेट रेसिपी पर चलती हों।",
            "अनहेयरिंग लाइम में काम करने वाली टैंनरी के लिए 80 ग्रेड कीमत का जवाब है; बड़े लाइन में कास्टिसाइज़िंग वाले काग़ज़ के मिल के लिए 90 वह जगह है जहाँ आपकी कास्टिक स्पेक तंग हो। अपनी रेसिपी के ख़िलाफ़ अक्षय सैंपल से पहले पुष्टि करेंगे।"],
        "use": [
            "काग़ज़ के प्लांट लाइम को रिकवरी साइकिल और कास्टिसाइज़िंग में इस्तेमाल करते हैं। टैंनरी इसे अनहेयरिंग लाइम में डोज़ करती है ताकि छिलके के बाल ढीले होकर हट जाएँ। कपड़े के प्लांट इसे रंगाई, स्कॉरिंग और फ़िनिशिंग की नहानियों में इस्तेमाल करते हैं, जहाँ स्थिर अल्कलाई रंग को एक जैसा रखती है।",
            "तीनों महीन, आसानी से बहने वाले पाउडर पर चलते हैं, इसलिए हम ग्रेड की महीनता को आपकी डोज़िंग विधि से मिलाते हैं, छोटे बैग से जंबो तक।"],
    },
    "agriculture": {
        "en_name": "Agriculture", "h1": "कृषि के लिए हाइड्रेटेड लाइम",
        "lede": "मिट्टी के pH का सुधार और खाद की तैयारी: रेंज की बल्क, किफ़ायती तरफ़, जहाँ 80 ग्रेड ज़्यादातर फ़सलों का काम-का ग्रेड है।",
        "why": [
            "खेत में प्रयोग एक मात्रा-कीमत का फैसला है, इसलिए 80 ग्रेड मानक कृषि चयन है: हमारी रेंज में सबसे कम टन-प्रति लागत पर 80 % न्यूनतम Ca(OH)₂।",
            "खाद में मिलाने या संवेदनशील फ़सलों पर डालने वाले मिट्टी-संशोधन के लिए कुछ ख़रीदार साफ़ उत्पाद के लिए 85 पर कदम बढ़ाते हैं; हम आपके मिट्टी रिपोर्ट से पुष्टि करके तय करेंगे।"],
        "use": [
            "हाइड्रेटेड लाइम ख़ट्टी मिट्टी का pH बढ़ाता है, पोषक तत्वों की उपलब्धता बढ़ाता है, और जड़ों के लिए बेहतर ग्रोथ के लिए मिट्टी को कंडीशन करता है। यह लाइम-आधारित खादों की तैयारी में भी इस्तेमाल होता है।",
            "कृषि के ख़रीदार आमतौर पर 25 से 40 किलो के बैग लेते हैं; अपने सीज़न की मात्रा पहले बताइए ताकि ज़रूरत पड़ने पर ऑर्डर तैयार हो।"],
    },
}

FAQ_HI = [
    ("मुझे कौन सा ग्रेड चाहिए?", "ऊपर अपना उद्योग देखें और लाल रंग में दिखाए ग्रेड से शुरू करें। फिर हमें अपनी प्रक्रिया बताइए: हम सही ग्रेड सुझाएँगे और उसका सैंपल CoA के साथ भेजेंगे, ताकि आप ख़ुद जाँच सकें।"),
    ("ग्रेड नंबर न्यूनतम है या औसत?", "न्यूनतम। ग्रेड नंबर Ca(OH)₂ की न्यूनतम मात्रा है, और हर लॉट के साथ CoA आता है जिसमें मापा गया परिणाम लिखा होता है।"),
    ("क्विकलाइम और हाइड्रेटेड लाइम में क्या अंतर है?", "क्विकलाइम कैल्शियम ऑक्साइड (CaO) है, जिसे कली चूना भी कहते हैं। हाइड्रेटेड लाइम उसी क्विकलाइम को नपे-तुले पानी से बुझाकर बना सूखा कैल्शियम हाइड्रॉक्साइड, Ca(OH)₂ है। इसे संभालना ज़्यादा सुरक्षित और डोज़ करना आसान है।"),
    ("क्या आप सैंपल भेजते हैं?", "हाँ। किसी भी ग्रेड का सैंपल उसके CoA के साथ भेजा जाता है। आप अपने प्लांट या लैब में जाँच लें, फिर उसी स्वीकृत सैंपल के अनुसार हम सप्लाई करते हैं।"),
    ("हाइड्रेटेड लाइम को कितने समय तक रख सकते हैं?", "सील बंद बैग में, सूखी और ठंडी जगह पर, छह महीने के भीतर इस्तेमाल करें। हवा की नमी और CO₂ से चूने का असरदार ग्रेड धीरे-धीरे घटता है।"),
]


def build(B):
    href, lic, wa, page = B.href, B.lic, B.wa, B.page

    def link(root, target):
        pg, _, anchor = target.partition("#")
        return href(root, pg) + (f"#{anchor}" if anchor else "")

    def ticker(root):
        items = "".join(f'<li><a href="{link(root, t)}"><b>{tag}</b> {txt} <span class="tk-go">{lbl}</span></a></li>' for tag, txt, t, lbl in TICKER_HI)
        items += "".join(f"<li>{t}</li>" for t in TICKER_HI_EXTRA)
        return f'''<div class="ticker ticker-top" role="region" aria-label="घोषणाएँ">
<div class="ticker-view"><div class="ticker-track"><ul>{items}</ul><ul aria-hidden="true" inert>{items}</ul></div></div>
<button class="ticker-btn" type="button" aria-pressed="false" aria-label="चलता टेक्स्ट रोकें">{lic("pause", "ic i-pause")}{lic("play", "ic i-play")}</button>
</div>'''

    def header(root, current, en_path):
        cur = ' aria-current="page"'
        links = "".join(f'<a href="{href(root, p)}"{cur if p == current else ""}{"" if p.startswith("hi/") else " hreflang=en"}>{t}</a>' for p, t in NAV_HI)
        en = f'{root}{en_path}' if en_path else root
        return f'''<a class="skip" href="#main">सीधे सामग्री पर जाएँ</a>
<div class="site-top">
{ticker(root)}
<header class="site-head">
<div class="wrap head-row">
{B.brand(root).replace('href="' + href(root, '') + '"', 'href="' + href(root, 'hi') + '"', 1)}
<nav class="nav" aria-label="मुख्य">{links}<a class="lang-switch" href="{en}" hreflang="en" lang="en">English</a><a class="btn btn-solid" href="{href(root, 'hi/contact')}">भाव पूछें</a></nav>
<a class="lang-switch lang-mob" href="{en}" hreflang="en" lang="en">English</a>
<details class="menu"><summary aria-label="मेन्यू खोलें">{lic("menu")}मेन्यू</summary><nav class="menu-panel" aria-label="मेन्यू">
<a href="{href(root, 'hi')}"{cur if current == 'hi' else ''}>होम</a>{links}<a href="{href(root, 'hi')}#brochure">ब्रोशर (PDF)</a>
<div class="menu-contact"><a class="btn btn-line" href="tel:{B.PHONE_TEL}">{lic("phone")}कॉल करें</a><a class="btn btn-wa" href="{B.WHATSAPP}">{lic("message-circle")}व्हाट्सऐप</a></div>
<a class="btn btn-solid" href="{href(root, 'hi/contact')}">भाव पूछें</a></nav></details>
</div>
</header>
</div>'''

    def footer(root):
        return f'''<footer class="site-foot">
<div class="wrap foot-grid">
<div>{B.brand(root, dark=True)}<p>हाइड्रेटेड लाइम के चार ग्रेड, जोधपुर के रणसीगांव में हमारे अपने प्लांट में बने।</p></div>
<div><h2>उत्पाद</h2><ul><li><a href="{href(root, 'hi/hydrated-lime')}">हाइड्रेटेड लाइम ग्रेड</a></li><li><a href="{B.brochure_href(root, 'lime')}" download>हाइड्रेटेड लाइम ब्रोशर (PDF, अंग्रेज़ी)</a></li><li><a href="{href(root, 'hydroxyapatite')}" hreflang="en">हाइड्रॉक्सीएपेटाइट</a></li><li><a href="{href(root, 'export')}" hreflang="en">एक्सपोर्ट और भाव</a></li></ul></div>
<div><h2>कंपनी</h2><ul><li><a href="{href(root, 'documents')}" hreflang="en">दस्तावेज़ (GST, IEC)</a></li><li><a href="{href(root, 'hi/contact')}">भाव पूछें</a></li><li>ऑफ़िस: {B.OFFICE}</li></ul></div>
<div><h2>संपर्क</h2><ul><li><a href="tel:{B.PHONE_TEL}">{B.PHONE_DISPLAY}</a></li><li><a href="{B.WHATSAPP}">व्हाट्सऐप करें</a></li><li><a href="mailto:{B.EMAIL}">{B.EMAIL}</a></li></ul></div>
</div>
<div class="wrap foot-base">© 2026 Calvara Labs &amp; Minerals · GSTIN {B.GSTIN} · HSN 2522 · CAS 1305-62-0</div>
</footer>'''

    def cta(root, title="जिस ग्रेड की ज़रूरत है, उसका सैंपल माँगें",
            text="अपना उपयोग, महीने की मात्रा और जो ग्रेड आप सोच रहे हैं, बताइए। जवाब सीधे हमारे इंजीनियर से आएगा, सैंपल और उसके CoA के साथ।"):
        return f'''<section class="cta-band"><div class="wrap cta-grid">
<div><h2>{title}</h2><p>{text}</p></div>
<div class="btn-row"><a class="btn btn-red" href="{href(root, 'hi/contact')}">भाव पूछें</a><a class="btn btn-ghost-light" href="{B.WHATSAPP}">व्हाट्सऐप करें</a></div>
</div></section>'''

    def hpage(path, root, current, en_path, title, desc, body, noindex=False, head_extra="", extra_ld=None):
        page(path, root, current, title, desc, body, lang="hi", alt=en_path, noindex=noindex,
             head_html=header(root, current, en_path), foot_html=footer(root), ui=UI,
             head_extra=head_extra, extra_ld=extra_ld)

    def ladder():
        rows = ""
        for i, (g, _l, _ca, _c, _m, si, _mesh) in enumerate(B.GRADES):
            pct = (int(g) - 70) / 22 * 100
            rows += f'<li><span class="g">{g}</span><span class="bar" aria-hidden="true"><i style="width:{pct:.0f}%;--row:{i}"></i></span><span class="si">सिलिका ≤ {si}</span></li>'
        return f'''<div class="ladder" role="group" aria-label="हाइड्रेटेड लाइम के चार ग्रेड">
<div class="ladder-head">चार ग्रेड<span>न्यूनतम % Ca(OH)<sub>2</sub></span></div>
<ol>{rows}</ol>
<div class="ladder-foot">ऊँचे ग्रेड में सक्रिय चूना ज़्यादा और सिलिका कम होती है, इसलिए कम मात्रा में काम हो जाता है।</div>
</div>'''

    def stats():
        return '''<div class="stats">
<div><b>4</b><span>शुद्धता ग्रेड, 80 से 92 %</span></div>
<div><b>92 %</b><span>सबसे ऊँची शुद्धता, न्यूनतम Ca(OH)<sub>2</sub></span></div>
<div><b>98.5 %</b><span>200 मेश से पार (92 ग्रेड)</span></div>
<div><b>25–40</b><span>किलो के बैग: 25, 30, 35 या 40 किलो, पैलेट पर या बिना पैलेट</span></div>
</div>'''

    def industries():
        out = ""
        for name, _use, gs in B.INDUSTRIES:
            hn, hu = IND_HI[name]
            chips = "".join(f'<li class="chip{" first" if i == 0 else ""}">{g}</li>' for i, g in enumerate(gs))
            slug = B.IND_SLUG[name]
            out += f'<div>{lic(B.IND_ICON.get(name, "factory"), "ic ind-ic")}<h3>{hn}</h3><p>{hu}</p><ul class="chips" aria-label="सुझाए गए ग्रेड, पहला ग्रेड शुरुआत के लिए">{chips}</ul><a class="ind-link" href="{href(root, "hi/industries/" + slug)}">{hn} के लिए ग्रेड पेज →</a></div>'
        return f'<div class="inds">{out}</div>'

    def faq():
        return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ_HI) + "</div>"

    def nextup():
        cards = [
            ("hydrated-lime", "हाइड्रेटेड लाइम", "ग्रेड और स्पेसिफ़िकेशन, उद्योग के हिसाब से इस्तेमाल, भंडारण और ग्रेड-दर-ग्रेड डेटा टैबल।", "स्पेसिफ़िकेशन देखें"),
            ("hi/industries", "उद्योग के अनुसार", "दस इस्तेमाल के पेज: पानी, एफ्लुएंट, चीनी, स्टील और और — कौन सा ग्रेड, क्यों और कैसे इस्तेमाल।", "अपना उपयोग खोजें"),
            ("export", "भाव और एक्सपोर्ट", "CIF, CFR और FOB शर्तें, कंटेनर की मात्रा, पैकिंग, और तैयार पूछताछ।", "एक्सपोर्ट विवरण देखें"),
            ("documents", "दस्तावेज़", "GST, IEC और MSME पंजीकरण, और स्वतंत्र लैब रिपोर्ट, हर एक की वेरिफ़ाई लिंक के साथ।", "दस्तावेज़ खोलें"),
            ("hydroxyapatite", "हाइड्रॉक्सीएपेटाइट", "टूथपेस्ट, टैबलेट और लैब के लिए एनिमल-फ्री HAp। माइक्रो ग्रेड सैंपल उपलब्ध, 250 ग्राम CoA के साथ।", "सैंपल माँगें"),
        ]
        out = "".join(f'<a class="nextup-card" href="{href(root, pg)}"{"" if pg.startswith("hi/") else ' hreflang="en"'}><h3>{t}</h3><p>{d}</p><span class="go">{g}</span></a>' for pg, t, d, g in cards)
        return f'<div class="nextup">{out}</div>'

    def start_steps_hi(root):
        return B.buy_steps([
            ("अपना उपयोग बताइए", "अपनी प्रक्रिया, महीने की मात्रा और जो ग्रेड आप सोच रहे हैं, यह साझा करें।"),
            ("सैंपल की जाँच करें", "हम सैंपल और उसका CoA भेजते हैं। आप इसे अपनी प्रक्रिया या लैब में जाँच करें।"),
            ("स्वीकृत करके ऑर्डर करें", "हम स्वीकृत सैंपल के अनुसार सप्लाई करते हैं, हर लॉट के साथ CoA।"),
        ])

    def hi_industry(slug):
        c = IND_HI_CONTENT[slug]
        en = B.IND_CONTENT[slug]
        root = "../../../"  # page lives at /hi/industries/<slug>/ — three levels deep
        g = next(row for row in B.GRADES if row[0] == en["grade"])
        others = "".join(
            f'<a class="nextup-card" href="{href(root, "hi/industries/" + s)}"><h3>{IND_HI_CONTENT[s]["h1"]}</h3><p>{IND_HI_CONTENT[s]["lede"]}</p><span class="go">पेज देखें</span></a>'
            for s in B.IND_ORDER if s != slug)
        body = f'''
<section class="page-head"><div class="wrap">
<nav class="crumbs" aria-label="आप यहाँ हैं"><a href="{href(root, 'hi')}">होम</a> / <a href="{href(root, 'hi/industries')}">उद्योग</a> / <span aria-current="page">{c["h1"].split(" के लिए")[0]}</span></nav>
<div class="page-head-grid">
<div class="prose" style="gap:16px">
<h1>{c["h1"]}</h1>
<p class="lede">{c["lede"]}</p>
<div class="btn-row"><a class="btn btn-solid" href="#quote">भाव पाएँ</a><a class="btn btn-line" href="{href(root, 'hi/hydrated-lime')}#spec">सारे ग्रेड की तुलना</a></div>
</div>
<div class="mini-tile"><span class="formula">ग्रेड {en["grade"]}</span><span class="meta">शुरुआत के लिए सुझाए गए ग्रेड</span><span class="meta">Ca(OH)<sub>2</sub> {g[2]} न्यूनतम · सिलिका ≤ {g[5]}</span></div>
</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>कौन सा ग्रेड, और क्यों</h2><p class="lede">हम आपको नीचे दिए ग्रेड से शुरू करवाते हैं, फिर सैंपल से आपकी प्रक्रिया के ख़िलाफ़ पुष्टि करते हैं।</p></div>
<div class="prose" style="max-width:760px">{"".join(f"<p>{p}</p>" for p in c["why"])}</div>
<p style="margin-top:18px"><a class="btn btn-line" href="{href(root, 'hi/hydrated-lime')}#spec">ग्रेड-दर-ग्रेड पूरी स्पेसिफ़िकेशन</a></p>
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>इसका इस्तेमाल कैसे होता है</h2></div>
<div class="prose" style="max-width:760px">{"".join(f"<p>{p}</p>" for p in c["use"])}</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>शुरुआत कैसे करें</h2><p class="lede">तीन क़दम, पहले सैंपल।</p></div>
{start_steps_hi(root)}
</div></section>

<section class="section section-tint" id="quote"><div class="wrap">
{quote(root)}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>अन्य उपयोग</h2></div>
<div class="nextup">{others}</div>
</div></section>

{cta(root)}'''
        service_ld = {"@context": "https://schema.org", "@type": "Service", "name": c["h1"], "description": c["lede"],
                      "inLanguage": "hi", "serviceType": f"hydrated lime supply, {en['name'].lower()}",
                      "provider": {"@type": "Organization", "name": "Calvara Labs & Minerals", "url": B.SITE},
                      "areaServed": "IN", "url": B.SITE + f"/hi/industries/{slug}/"}
        hpage(f"hi/industries/{slug}", root, f"hi/industries/{slug}", f"industries/{slug}/",
              c["h1"] + " | Calvara Labs, जोधपुर", c["lede"], body, extra_ld=service_ld)

    def hi_industry_index():
        root = "../../"  # page lives at /hi/industries/ — two levels deep
        cards = ""
        for s in B.IND_ORDER:
            c = IND_HI_CONTENT[s]
            icon = lic(B.IND_ICON.get(c["en_name"], "factory"), "ic ind-ic")
            cards += f'<a class="nextup-card" href="{href(root, "hi/industries/" + s)}">{icon}<h3>{c["h1"]}</h3><p>ग्रेड {B.IND_CONTENT[s]["grade"]} से शुरू; सैंपल और CoA से आपकी प्रक्रिया के ख़िलाफ़ पुष्टि।</p><span class="go">पेज पढ़ें</span></a>'
        body = f'''
<section class="page-head"><div class="wrap">
<nav class="crumbs" aria-label="आप यहाँ हैं"><a href="{href(root, 'hi')}">होम</a> / <span aria-current="page">उद्योग</span></nav>
<div class="prose" style="gap:14px;max-width:760px">
<h1>उद्योग के अनुसार हाइड्रेटेड लाइम</h1>
<p class="lede">दस उपयोग के पेज: कौन सा ग्रेड, क्यों, और आपकी प्रक्रिया में इसका इस्तेमाल कैसे होता है। अपने से शुरू करें और लाल में दिखे ग्रेड को अपने पहले सवाल में शामिल करें।</p>
<div class="btn-row"><a class="btn btn-solid" href="{href(root, 'hi/hydrated-lime')}#spec">उद्योग-दर-उद्योग ग्रेड टैबल</a><a class="btn btn-line" href="{href(root, 'hi/contact')}">अक्षय से पूछें</a></div>
</div>
</div></section>

<section class="section"><div class="wrap">
<div class="nextup">{cards}</div>
</div></section>

{cta(root)}'''
        hpage("hi/industries", root, "hi/industries", "industries/", "उद्योग के अनुसार हाइड्रेटेड लाइम | Calvara Labs, जोधपुर",
              "दस उद्योगों में कौन सा हाइड्रेटेड लाइम ग्रेड इस्तेमाल करें — पानी और एफ़्लुएंट, चीनी, केमिकल, सिरामिक और काँच, फ़्लू गैस, निर्माण, स्टील, काग़ज़, चमड़ा, कपड़ा और कृषि।", body)

    def quote(root):
        s = B.quote_builder(root)
        for a, b in [
            ("<h2>Get a full quote in one message</h2>", "<h2>एक संदेश में पूरा भाव पाएँ</h2>"),
            ("Tap your choices and send. Akshay replies with price, specification, container quantity, lead time and payment terms together.",
             "अपने विकल्प चुनें और भेजें। अक्षय भाव, स्पेसिफ़िकेशन, डिलीवरी का समय और भुगतान की शर्तें एक साथ बताएँगे।"),
            ("<legend>Grade</legend>", "<legend>ग्रेड</legend>"), ("<legend>Packing</legend>", "<legend>पैकिंग</legend>"),
            ("<legend>Pallets</legend>", "<legend>पैलेट</legend>"), ("<legend>Price basis</legend>", "<legend>भाव का आधार</legend>"),
            ("kg bags", "किलो बैग"), ('"Not palletised"', '"बिना पैलेट"'), (">Not palletised<", ">बिना पैलेट<"),
            ('"Palletised"', '"पैलेट पर"'), (">Palletised<", ">पैलेट पर<"), ("Not sure", "पता नहीं"),
            ('value="CIF" checked', 'value="CIF"'), ('value="Delivered in India"', 'value="Delivered in India" checked'),
            ("Ex-works Jodhpur", "जोधपुर प्लांट से"), ("Delivered in India", "आपकी साइट तक"),
            (">Your port or city<", ">आपका शहर या पोर्ट<"), ('placeholder="Durban, Port Louis, Mombasa"', 'placeholder="जयपुर, अहमदाबाद, मुंद्रा पोर्ट"'),
            (">Quantity<", ">मात्रा<"), ('placeholder="1 x 20 ft a month"', 'placeholder="20 टन प्रति माह"'),
            (">Send on WhatsApp<", ">व्हाट्सऐप पर भेजें<"), (">Send by email<", ">ईमेल से भेजें<"),
            ("<span>Your message:</span>", "<span>आपका संदेश:</span>"),
            ("Hello Akshay, please quote hydrated lime.", "नमस्ते अक्षय जी, कृपया हाइड्रेटेड लाइम का भाव बताइए।"),
            ('"Grade: "', '"ग्रेड: "'), ('"please advise"', '"आप सुझाइए"'), ('"Packing: "', '"पैकिंग: "'),
            ('"Price basis: "', '"भाव का आधार: "'), ('"Quantity: "', '"मात्रा: "'), ('"to discuss"', '"बात करके तय करेंगे"'),
            ('"Please include container quantity, lead time, payment terms and the spec sheet."', '"कृपया डिलीवरी का समय, भुगतान की शर्तें और स्पेसिफ़िकेशन शीट भी भेजें।"'),
            ('"Hydrated lime quote: grade "', '"हाइड्रेटेड लाइम भाव: ग्रेड "'),
        ]:
            s = s.replace(a, b)
        return s

    def motion(root):
        s = B.motion_section(root)
        for a, b in [
            ("<h2>See how your lime is made</h2>", "<h2>देखिए आपका चूना कैसे बनता है</h2>"),
            ("From quicklime to a sealed bag at our plant in Ransigaon, Jodhpur. Plant visits are welcome by appointment.",
             "क्विकलाइम से सील बंद बैग तक, जोधपुर के रणसीगांव स्थित हमारे प्लांट में। समय लेकर प्लांट देखने ज़रूर आइए।"),
            ("<h3>Five steps, one roof</h3>", "<h3>पाँच क़दम, एक छत</h3>"),
            ("<b>The process</b>Quicklime and measured water become dry hydrated lime.", "<b>प्रक्रिया</b>क्विकलाइम और नपा-तुला पानी मिलकर सूखा हाइड्रेटेड लाइम बनते हैं।"),
            ("<h3>Kiln</h3>", "<h3>भट्टी</h3>"),
            ("Rajasthan limestone is burnt to quicklime (CaO) and drawn out onto the conveyor.",
             "राजस्थान का चूना पत्थर क्विकलाइम (CaO) में पकता है और कंवेयर पर आता है।"),
            ("<h3>Measured water</h3>", "<h3>नपा-तुला पानी</h3>"),
            ("Quicklime is fed to the hydrator with a metered flow of water.",
             "क्विकलाइम मीटर किया हुआ पानी के साथ हाइड्रेटर में जाता है।"),
            ("<h3>Hydrator</h3>", "<h3>हाइड्रेटर</h3>"),
            ("Quicklime is slaked into dry calcium hydroxide, Ca(OH)₂, in a rotating drum.",
             "क्विकलाइम घूमते ड्रम में सूखा कैल्शियम हाइड्रॉक्साइड, Ca(OH)₂, बन जाता है।"),
            ("<h3>Classifier</h3>", "<h3>क्लासिफ़ायर</h3>"),
            ("Fine powder passes on; grit and silica are dropped out, so fineness stays within the grade.",
             "महीन पाउडर आगे जाता है; गिट्टी और सिलिका बाहर गिरती है, इसलिए महीनता ग्रेड के अंदर रहती है।"),
            ("<h3>Packing</h3>", "<h3>पैकिंग</h3>"),
            ("25 to 40 kg bags and 900 kg jumbo bags, filled under a bag-filter dust collector.",
             "25 से 40 किलो के बैग और 900 किलो के जंबो बैग, बैग-फ़िल्टर डस्ट कलेक्टर के नीचे भरते हैं।"),
            ("<b>Why you should care:</b> because the same plant runs the kiln, the hydrator and the lab, every lot can be tested and shipped with its own Certificate of Analysis.",
             "<b>यह क्यों देखें:</b> इसी प्लांट में भट्टी, हाइड्रेटर और लैब चलते हैं, इसलिए हर लॉट की जाँच होकर उसके अपने CoA के साथ भेजा जा सकता है।"),
            ("<b>Watch the plant run</b>", "<b>प्लांट चलते देखें</b>"),
            ("<b>Inside the plant</b>Kiln, hydrators, classifier, packing and the plant lab.", "<b>प्लांट के अंदर</b>भट्टी, हाइड्रेटर, क्लासिफ़ायर, पैकिंग और प्लांट लैब।"),
            ("<b>Packing and dispatch</b>25 to 40 kg bags and 900 kg jumbo bags, ready stock.", "<b>पैकिंग और डिस्पैच</b>25 से 40 किलो के बैग और 900 किलो के जंबो बैग, तैयार स्टॉक।"),
            ("Swipe to see all three.", "तीनों देखने के लिए स्वाइप करें।"),
            ('aria-label="Pause process animation"', 'aria-label="प्रक्रिया एनिमेशन रोकें"'),
            ('aria-label="Pause inside the plant"', 'aria-label="प्लांट वीडियो रोकें"'),
            ('aria-label="Pause packing and dispatch"', 'aria-label="पैकिंग वीडियो रोकें"'),
        ]:
            s = s.replace(a, b)
        return s

    def brochures(root):
        s = B.brochure_block(root)
        for a, b in [
            ("Free download", "मुफ़्त डाउनलोड"),
            (">Hydrated Lime Brochure<", ">हाइड्रेटेड लाइम ब्रोशर<"),
            (">Hydroxyapatite Brochure<", ">हाइड्रॉक्सीएपेटाइट ब्रोशर<"),
            ("All 4 grades and specs, plant photos, packing, export loading and CoA format.",
             "चारों ग्रेड और उनकी स्पेसिफ़िकेशन, प्लांट की तस्वीरें, पैकिंग, लोडिंग और CoA का फ़ॉर्मेट। ब्रोशर अंग्रेज़ी में है।"),
            ("Micro and nano grades, full specification, how we make it, and how to start with a 250 g sample.",
             "माइक्रो और नैनो ग्रेड, पूरी स्पेसिफ़िकेशन, बनाने का तरीका और 250 ग्राम के सैंपल से शुरुआत। ब्रोशर अंग्रेज़ी में है।"),
            ("Download brochure (PDF)", "ब्रोशर डाउनलोड करें (PDF)"), (">View online<", ">ऑनलाइन देखें<"),
            ("10 pages · PDF", "10 पेज · PDF"), ("6 pages · PDF", "6 पेज · PDF"),
            ('aria-label="View the Hydrated Lime Brochure online"', 'aria-label="हाइड्रेटेड लाइम ब्रोशर ऑनलाइन देखें"'),
            ('aria-label="View the Hydroxyapatite Brochure online"', 'aria-label="हाइड्रॉक्सीएपेटाइट ब्रोशर ऑनलाइन देखें"'),
            ('aria-label="Brochures"', 'aria-label="ब्रोशर"'),
        ]:
            s = s.replace(a, b)
        return s

    def engineer(root):
        img = B.photo("akshay")
        av = f'<img class="avatar" src="{img}" alt="अक्षय खदाव" loading="lazy" width="84" height="84" style="padding:0">' if img else ""
        return f'''<div class="engineer">{av}<div>
<blockquote>“अपनी प्रक्रिया के बारे में बताइए। मैं सही ग्रेड सुझाऊँगा, और सैंपल भेजकर दिखाऊँगा कि वह काम करता है।”</blockquote>
<p class="eng-name"><b>अक्षय खदाव</b><span>बी.टेक केमिकल इंजीनियरिंग, IIT&nbsp;बॉम्बे</span></p>
<p>आप हमें लिखते हैं तो सीधे मुझसे बात होती है: केमिस्ट्री, ग्रेड और डिस्पैच, किसी कॉल सेंटर से नहीं।</p>
<div class="btn-row"><a class="btn btn-red" href="{B.WHATSAPP}">अक्षय को व्हाट्सऐप करें</a><a class="btn btn-ghost-light" href="tel:{B.PHONE_TEL}">कॉल करें {B.PHONE_DISPLAY}</a></div>
</div></div>'''

    def crumbs(root, name):
        return f'<nav class="crumbs" aria-label="आप यहाँ हैं"><a href="{href(root, "hi")}">होम</a> / <span aria-current="page">{name}</span></nav>'

    # ---------- /hi/ home ----------
    root = "../"
    body = f'''
<section class="hero hero-video"><video class="hero-bg" muted loop playsinline preload="none" poster="{root}assets/media/hero-bg-poster.webp" aria-hidden="true"><source src="{root}assets/media/hero-bg.webm" type="video/webm"><source src="{root}assets/media/hero-bg.mp4" type="video/mp4"></video><div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow-plain">हाइड्रेटेड लाइम · जोधपुर, राजस्थान</p>
<h1>आपकी ज़रूरत के ग्रेड का हाइड्रेटेड लाइम</h1>
<p class="lede">80 से 92 % Ca(OH)<sub>2</sub> तक चार ग्रेड, जोधपुर के रणसीगांव में हमारे अपने प्लांट में बने। हर लॉट की जाँच हमारी प्लांट लैब में होती है और उसके साथ सर्टिफ़िकेट ऑफ़ एनालिसिस (CoA) आता है।</p>
<div class="btn-row"><a class="btn btn-solid" href="#quote">भाव पूछें</a><a class="btn btn-red" href="{B.brochure_href(root, 'lime')}" download>{lic("download")}ब्रोशर डाउनलोड करें</a></div>
</div>
<div class="hero-ladder">{ladder()}</div>
</div></section>
{B.marquee(["चार ग्रेड", "80 से 92 % Ca(OH)<sub>2</sub>", "हर लॉट की जाँच", "हर डिस्पैच के साथ CoA", "जोधपुर, राजस्थान में निर्मित", "पहले सैंपल, फिर ऑर्डर"], "lg", speed=55)}

{motion(root)}

<section class="broch-band" id="brochure"><div class="wrap">
{brochures(root)}
</div></section>

<section><div class="wrap">{stats()}</div></section>

<section class="section section-tint" id="quote"><div class="wrap">
{quote(root)}
</div></section>

<section class="section"><div class="wrap split">
<div class="prose">
<h2>हमारा अपना प्लांट, एक इंजीनियर की देखरेख में</h2>
<p>Calvara Labs &amp; Minerals जोधपुर की चूना पट्टी में बसे रणसीगांव में अपने प्लांट पर हाइड्रेटेड लाइम बनाती है। चूना पत्थर, भट्टी और लैब जाँच हमारा रोज़ का काम है।</p>
<p>हर ग्रेड की स्पेसिफ़िकेशन तय है। पहले आप सैंपल जाँचते हैं, फिर हम उसी स्वीकृत सैंपल के अनुसार सप्लाई करते हैं।</p>
<ul><li><b>भट्टी का अनुभव।</b> अपनी भट्टी चलाने से हम चूना पत्थर, पकाई और कैल्शियम केमिस्ट्री को अच्छी तरह जानते हैं।</li><li><b>जाँच, अंदाज़ा नहीं।</b> हर लॉट प्लांट लैब में जाँचा जाता है और CoA के साथ भेजा जाता है।</li><li><b>पहले सैंपल।</b> नियमित ऑर्डर से पहले ग्रेड को अपनी प्रक्रिया में आज़माइए।</li></ul>
</div>
{engineer(root)}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>आगे की जानकारी</h2><p class="lede">यह पेज छोला रखते हैं। विस्तार नीचे दिए पेजों पर है।</p></div>
{nextup()}
</div></section>

{cta(root)}'''
    hpage("hi", root, "hi", "", "हाइड्रेटेड लाइम निर्माता, जोधपुर | ग्रेड 80–92 | Calvara Labs",
          "जोधपुर के अपने प्लांट में बना हाइड्रेटेड लाइम, चार ग्रेड: 80 से 92 % Ca(OH)2। सिलिका 1.06 % से, 98.5 % तक 200 मेश से पार, हर लॉट के साथ CoA।", body, head_extra=B.hero_preload(root))

    # ---------- /hi/hydrated-lime/ ----------
    root = "../../"
    labels = [("Ca(OH)<sub>2</sub> मात्रा, न्यूनतम", 2), ("समतुल्य CaO (गणना से)", 3), ("नमी, अधिकतम", 4),
              ("एसिड अघुलनशील (सिलिका), अधिकतम", 5), ("200 मेश (75 µm) से पार, न्यूनतम", 6)]
    head = "".join(f'<th scope="col"><span class="gn">{g[0]}</span>ग्रेड</th>' for g in B.GRADES)
    rows = "".join(f'<tr><th scope="row">{lab}</th>' + "".join(f'<td class="num">{g[i]}</td>' for g in B.GRADES) + "</tr>" for lab, i in labels)
    table = f'<div class="table-box"><table class="spec-wide"><caption>ग्रेड के अनुसार सामान्य स्पेसिफ़िकेशन</caption><thead><tr><th scope="col">पैरामीटर</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    bags = "".join(f'<li><b>{k} किलो</b><span>लाइनर वाला लैमिनेटेड बैग</span></li>' for k in (25, 30, 35, 40))
    bags = f'<ul class="bags">{bags}<li class="jumbo"><b>पैलेट</b><span>पैलेट पर या बिना पैलेट</span></li></ul>'
    body = f'''
<section class="page-head"><div class="wrap">
{crumbs(root, "हाइड्रेटेड लाइम")}
<h1>हाइड्रेटेड लाइम के चार ग्रेड</h1>
<p class="lede">कैल्शियम हाइड्रॉक्साइड, Ca(OH)<sub>2</sub>। जोधपुर, राजस्थान की चूना पट्टी से बना महीन, सूखा और उच्च शुद्धता वाला पाउडर। हर लॉट की जाँच होती है, उस पर लेबल लगता है और ग्रेड आपकी ज़रूरत के अनुसार बनता है।</p>
<div class="btn-row"><a class="btn btn-red" href="{B.brochure_href(root, 'lime')}" download>{lic("download")}ब्रोशर डाउनलोड करें (PDF)</a><a class="btn btn-line" href="#spec">ग्रेड की तुलना करें</a></div>
</div></section>
{B.marquee([f"ग्रेड {g[0]}" for g in B.GRADES], "lg", speed=40)}

<section class="section" id="spec"><div class="wrap">
<div class="section-head"><h2>ग्रेड के अनुसार स्पेसिफ़िकेशन</h2><p class="lede">ग्रेड नंबर Ca(OH)<sub>2</sub> की न्यूनतम मात्रा है। ऊँचे ग्रेड में सिलिका कम और पाउडर ज़्यादा महीन होता है।</p></div>
{table}
<p class="swipe-hint">पूरी तालिका देखने के लिए स्वाइप करें।</p>
<p class="note" style="margin-top:14px;font-size:14px;color:var(--ink-soft)">ये सामान्य, संकेतात्मक मान हैं। अंतिम स्पेसिफ़िकेशन स्वीकृत सैंपल और हर लॉट के CoA से तय होती है।</p>
</div></section>

<section class="section section-tint" id="quote"><div class="wrap">
{quote(root)}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>उद्योग के अनुसार ग्रेड चुनें</h2><p class="lede">लाल रंग वाले ग्रेड से शुरुआत करें।</p></div>
{industries()}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>पैकिंग आपकी पसंद की</h2><p class="lede">सील बंद, लैमिनेटेड बैग, अंदर लाइनर के साथ, ताकि आपके प्लांट तक चूना सूखा रहे।</p></div>
{bags}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>भंडारण और सुरक्षित इस्तेमाल</h2></div>
<div class="facts facts-3">
<div><b>सूखा और सील बंद रखें</b><p>ठंडी, सूखी जगह पर, मूल सील बंद बैग में रखें। दीवार से हटाकर पैलेट पर चट्टा लगाएँ।</p></div>
<div><b>छह महीने के भीतर इस्तेमाल करें</b><p>चूना हवा से धीरे-धीरे CO<sub>2</sub> और नमी सोखता है, जिससे असरदार ग्रेड घटता है।</p></div>
<div><b>सावधानी से संभालें</b><p>क्षारीय पदार्थ: त्वचा, आँख और साँस में जलन कर सकता है। दस्ताने, चश्मा और डस्ट मास्क पहनें। संपर्क होने पर खूब पानी से धोएँ।</p></div>
</div>
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>ख़रीदारों के आम सवाल</h2></div>
{faq()}
</div></section>

{cta(root, "हाइड्रेटेड लाइम का भाव पाएँ", "ग्रेड, महीने की मात्रा और डिलीवरी का शहर बताइए। जवाब सीधे हमारे इंजीनियर से आएगा।")}'''
    hpage("hi/hydrated-lime", root, "hi/hydrated-lime", "hydrated-lime/", "हाइड्रेटेड लाइम ग्रेड 80–92 % | स्पेसिफ़िकेशन | Calvara Labs, जोधपुर",
          "हाइड्रेटेड लाइम के चार ग्रेड: Ca(OH)2 80–92 %, सिलिका 1.06–8 %, नमी 0.8–2.0 %, 90–98.5 % तक 200 मेश से पार। 25 से 40 किलो के बैग, हर लॉट के साथ CoA।", body)

    # ---------- /hi/contact/ ----------
    grade_opts = "".join(f"<option>ग्रेड {g[0]}</option>" for g in B.GRADES)
    auto = ("Calvara Labs & Minerals से संपर्क करने के लिए धन्यवाद। हमारे केमिकल इंजीनियर अक्षय खदाव को आपकी पूछताछ मिल गई है "
            "और वे भाव, स्पेसिफ़िकेशन और डिलीवरी समय के साथ जल्द जवाब देंगे, अक्सर उसी दिन।\n\n"
            "तब तक हमारे ब्रोशर देखें (अंग्रेज़ी में):\n"
            "हाइड्रेटेड लाइम: https://calvaralabs.com/brochures/Calvara-Hydrated-Lime-Brochure-2026.pdf\n"
            "हाइड्रॉक्सीएपेटाइट: https://calvaralabs.com/brochures/Calvara-Hydroxyapatite-Brochure-2026.pdf\n\n"
            "जल्दी जवाब के लिए व्हाट्सऐप करें: +91 98927 27068\n\n"
            "Calvara Labs & Minerals, जोधपुर, राजस्थान · calvaralabs.com")
    body = f'''
<section class="page-head"><div class="wrap">
{crumbs(root, "संपर्क")}
<div class="prose" style="gap:14px;max-width:760px">
<h1>चूने की बात करें</h1>
<p class="lede">सैंपल, स्पेसिफ़िकेशन शीट या ग्रेड की सलाह माँगिए। जवाब सीधे एक इंजीनियर से मिलेगा।</p>
<div class="btn-row"><a class="btn btn-wa" href="{B.WHATSAPP}">व्हाट्सऐप {B.PHONE_DISPLAY}</a><a class="btn btn-line" href="{href(root, 'hi')}#quote">झटपट भाव</a></div>
</div>
</div></section>

<section class="section"><div class="wrap contact-grid">
<form class="form" action="https://formsubmit.co/{B.EMAIL}" method="POST">
<input type="hidden" name="_subject" value="नई पूछताछ (हिंदी पेज) calvaralabs.com">
<input type="hidden" name="_next" value="{B.SITE}/hi/thanks/">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_autoresponse" value="{auto}">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="field"><label for="f-name">आपका नाम</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="f-company">कंपनी (वैकल्पिक)</label><input id="f-company" name="company" type="text" autocomplete="organization"></div>
<div class="field"><label for="f-phone">फ़ोन या व्हाट्सऐप</label><input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required></div>
<div class="field"><label for="f-email">ईमेल</label><input id="f-email" name="email" type="email" inputmode="email" autocomplete="email"></div>
<div class="field"><label for="f-product">उत्पाद</label><select id="f-product" name="product"><option>हाइड्रेटेड लाइम</option><option>हाइड्रॉक्सीएपेटाइट</option><option>दोनों</option></select></div>
<div class="field"><label for="f-grade">ग्रेड</label><select id="f-grade" name="grade"><option>पता नहीं, आप सुझाइए</option>{grade_opts}</select></div>
<div class="field"><label for="f-request">मुझे चाहिए</label><select id="f-request" name="request"><option>सैंपल</option><option>भाव</option><option>स्पेसिफ़िकेशन शीट</option><option>ग्रेड की सलाह</option></select></div>
<div class="field"><label for="f-qty">महीने की मात्रा</label><input id="f-qty" name="quantity" type="text" placeholder="20 टन प्रति माह"></div>
<div class="field full"><label for="f-use">आपका उपयोग</label><input id="f-use" name="application" type="text" placeholder="पानी का ट्रीटमेंट, AAC ब्लॉक"></div>
<div class="field full"><label for="f-where">डिलीवरी का शहर</label><input id="f-where" name="delivery" type="text" autocomplete="address-level2"></div>
<div class="field full"><label for="f-msg">और कुछ (वैकल्पिक)</label><textarea id="f-msg" name="message" rows="3"></textarea></div>
<div class="actions"><button class="btn btn-red" type="submit">पूछताछ भेजें</button><p>आपकी जानकारी केवल इस पूछताछ का जवाब देने के लिए इस्तेमाल होती है।</p></div>
</form>
<aside style="display:flex;flex-direction:column;gap:20px">
<div class="side-card dark">
<h2 style="font-size:22px">आपके इंजीनियर</h2>
<p><b style="color:#fff">अक्षय खदाव</b><br>बी.टेक केमिकल इंजीनियरिंग, IIT&nbsp;बॉम्बे</p>
<div class="contact-line"><span>कॉल या व्हाट्सऐप</span><a href="tel:{B.PHONE_TEL}">{B.PHONE_DISPLAY}</a></div>
<div class="contact-line"><span>ईमेल</span><a href="mailto:{B.EMAIL}">{B.EMAIL}</a></div>
<div class="contact-line"><span>ऑफ़िस</span><p>{B.OFFICE}<br><a href="{B.MAPS}" target="_blank" rel="noopener">Google Maps पर देखें</a></p></div>
<div class="contact-line"><span>प्लांट</span><p>{B.WORKS}</p></div>
</div>
<div class="side-card light">
<h2 style="font-size:20px">हमसे माँगें</h2>
<ol><li>जिस ग्रेड को आप जाँचना चाहते हैं, उसका सैंपल</li><li>स्पेसिफ़िकेशन शीट और सर्टिफ़िकेट ऑफ़ एनालिसिस</li><li>आपकी प्रक्रिया के अनुसार ग्रेड की सलाह</li></ol>
</div>
</aside>
</div></section>
<script>
(function(){{var f=document.querySelector('.form');if(!f)return;var b=f.querySelector('button[type=submit]'),note=f.querySelector('.actions p');f.addEventListener('submit',function(){{b.disabled=true;b.textContent='भेज रहे हैं…';if(note)note.textContent='आपकी पूछताछ भेजी जा रही है — यह जल्द धन्यवाद पेज पर ले जाएगा।';}});}})();
</script>'''
    hpage("hi/contact", root, "hi/contact", "contact/", "संपर्क करें | हाइड्रेटेड लाइम का भाव, जोधपुर | Calvara Labs",
          "हाइड्रेटेड लाइम का सैंपल, भाव या स्पेसिफ़िकेशन माँगें। जोधपुर, राजस्थान। कॉल या व्हाट्सऐप +91 98927 27068।", body)

    # ---------- /hi/thanks/ ----------
    body = f'''
<section class="page-head"><div class="wrap">
<div class="prose" style="gap:14px;max-width:760px">
<h1>धन्यवाद, आपकी पूछताछ मिल गई है</h1>
<p class="lede">अक्षय जल्द ही जवाब देंगे, अक्सर उसी दिन। जल्दी बात करनी हो तो व्हाट्सऐप करें।</p>
<div class="btn-row"><a class="btn btn-wa" href="{B.WHATSAPP}">व्हाट्सऐप {B.PHONE_DISPLAY}</a><a class="btn btn-line" href="{href(root, 'hi')}">होम पर लौटें</a></div>
</div></div></section>'''
    hpage("hi/thanks", root, "", "thanks/", "धन्यवाद | Calvara Labs &amp; Minerals", "आपकी पूछताछ मिल गई है।", body, noindex=True)

    # ---------- /hi/industries/ + one page per industry ----------
    hi_industry_index()
    for _slug in B.IND_ORDER:
        hi_industry(_slug)
