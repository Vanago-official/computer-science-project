import streamlit as st

st.set_page_config(page_title="Bank Money Transfers", layout="wide")

st.markdown("""
    <style>
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
            padding-top: 25px;
        }

        div[data-baseweb="tab-panel"] div.stButton > button {
            height: 125px;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)


@st.dialog(" ", width="large")
def modal_window(contain):
    st.markdown(
        """
        <style>
        div[data-testid="stDialog"] div[role="dialog"] {
            width: fit-content;
            max-width: 50vw;
            min-width: 200px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
            <div style="
                word-wrap: break-word; 
                overflow-wrap: break-word;
                ">
                {contain}
            </div>
            """,
        unsafe_allow_html=True
    )


col1, col2, col3 = st.columns([0.15, 0.70, 0.15])
with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/6475/6475938.png",
        width=125,
    )
with col2:
    st.title("Bank Money Transfers")
    st.caption("Зроблено командою Counter Strike з любов'ю <3")

with col3:
    @st.dialog(" ", width="large")
    def authors_modal():
        st.markdown(
            """
            <style>
            div[data-testid="stDialog"] div[role="dialog"] {
                width: fit-content;
                max-width: 50vw;
                min-width: 200px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        ac1, ac2, ac3, ac4 = st.columns(4)

        with ac1:
            st.image("images/Lisa.jpg", use_container_width=True)
            st.subheader("Ушкевич Єлизавета")

        with ac2:
            st.image("images/Sqb.jpg", use_container_width=True)
            st.subheader("Скуб Анастасія")

        with ac3:
            st.image("images/Yulian.png", use_container_width=True)
            st.subheader("Главаті Юліан")

        with ac4:
            st.image("images/Ivan.JPEG", use_container_width=True)
            st.subheader("Новоселов Іван")


    # Основна логіка кнопки в col3
    with col3:
        if st.button("Автори", key="authores", use_container_width=True):
            authors_modal()

    if st.button("Джерела", key="sources", use_container_width=True):
        modal_window("""
        - https://zakon.rada.gov.ua/laws/show/2346-14#Text
        - https://business.diia.gov.ua/finance/handbook/scho-take-p2p-perekaz
        - https://torgsoft.ua/articles/stati/b2b-prodazhi/
        - https://handmade-hub.ua/shcho-take-b2b-i-b2c/
        - https://business-broker.com.ua/blog/shcho-take-rekvizyty-vyznachennia-pryklady-ta-poiasnennia/
        - https://privatbank.ua/iban
        - https://blog.easypay.ua/nomer-bankivskoyi-kartky-shho-hovayetsya-za-czyframy-ta-yak-cze-zahyshhaye-vashi-groshi/
        - https://lv.tax.gov.ua/media-ark/news-ark/533982.html
        - https://industrialbank.ua/ua/business/corporate/other/systemy-dystantsiinoho-obsluhovuvannia
        - https://www.eximb.com/ua/business/klientam-msb/msb-dystancijne-obslugovuvannya/msb-ifobs/
        - https://vchasno.ua/shcho-take-pos-terminal/
        - https://www.zen.com/ua/blog/shopping-uk/what-is-google-pay-settings-peculiarities/
        - https://news.dtkt.ua/state/cash-handling/58071-shho-take-bezgotivkovi-i-gotivkovi-rozraxunki-roziasniuje-nbu
        - https://fpk.in.ua/images/biblioteka/3fmb_finan/Babenko-Levada_The_banking_system.pdf
        - https://new.finance.ua/ua/bankers-day
        - https://uk.wikipedia.org/wiki/%D0%96%D0%B8%D1%80%D0%BE%D0%B1%D0%B0%D0%BD%D0%BA
        - https://essuir.sumdu.edu.ua/server/api/core/bitstreams/22913e44-dab0-444f-ab31-9f7f0ef3e999/content
        - https://logomaster.com.ua/index_uk.php?p=4287
        - https://worldbank.org.ua/4516-istoriya-uspikhu-mastercard.html
        - https://worldbank.org.ua/4539-istoriya-uspikhu-kompaniyi-visa.html
        - https://ash.kozak.cx.ua/maysternist/yak-pochinavsya-american-express.html
        - https://www.matriks-pres.com.ua/shcho-take-swift-slovo-vyznachennia-ta-iak-pratsiuie-systema/
        - https://worldbank.org.ua/4603-paypal.html
        - https://cryptomus.com/uk/blog/early-cryptocurrencies-what-were-they
        - https://www.binance.com/uk-UA/academy/articles/central-bank-digital-currencies-cbdc-explained
        - https://bank.gov.ua/ua/news/all/sistemi-elektronnih-platejiv-natsionalnogo-banku-vipovnilosya-25-rokiv
        - https://bank.gov.ua/ua/news/all/zapratsyuvala-modernizovana-sistema-elektronnih-platejiv-nbu
        - https://new.finance.ua/ua/30-rokiv-nezalezhnosti/monobank
        - https://www.codeproject.com/articles/Introduction-to-ISO
        - https://isaaclanre.medium.com/iso-8583-the-technical-foundation-of-modern-payment-systems-33af3fbaee68
        - https://bank.gov.ua/ua/payments/project-iso20022
        - https://www.iso20022.org/iso-20022-message-definitions
        - https://www2.swift.com/knowledgecentre/rest/v1/publications/usgi_20220722/2.0/usgi_20220722.pdf?logDownload=true
        - https://mixfin.com/ua/tops/najkrashhi-platizhni-sistemy-v-ukrayini/
        - https://docs.easypay.pt/#section/Single-Overview
        - https://wiki.wayforpay.com/
        - https://www.liqpay.ua/doc/api
        - https://docs.portmone.com.ua/docs/uk/PaymentGatewayUa
        - https://cdn-icons-png.flaticon.com/512/6475/6475938.png
        """)

tab1, tab2, tab3 = st.tabs(["Види переказів", "Історія переказів", "Сьогодення"])

with tab1:
    colA, colB, colC = st.columns(3)

    with colA:
        if st.button("Визначення та суть банківського переказу", key="1", use_container_width=True):
            modal_window("""
            Банківський переказ (або «переказ коштів») — це рух певної суми коштів. Метою цього руху є або її зарахування на рахунок отримувача, або видача йому у готівковій формі. Фактично, переказ — це певний процес, який може проходити декілька етапів залежно від мети переказу. У цьому процесі завжди бере участь банк. Чітких визначень видів переказів не існує, і їх можна розділяти на види, виходячи з різних кутів погляду.
            """)

    with colB:
        if st.button("Класифікація за учасниками переказу", key="2", use_container_width=True):
            modal_window("""
            Перекази можна розділити залежно від того, хто є платником та отримувачем коштів:
            - P2P (Person-to-Person): Переказ, що здійснюється від людини до людини.
            - B2B (Business-to-Business): Переказ, що здійснюється від підприємства до підприємства.
            - B2C (Business-to-Consumer): Переказ, що здійснюється від людини до підприємства, зазвичай це є звичайними покупками чи сплатою за послуги
            ![](https://i.postimg.cc/Tw13yJZL/Slide-16-9-2.png)
""")

    with colC:
        if st.button("Класифікація за способами ідентифікації отримувача", key="3", use_container_width=True):
            modal_window("""
            Ідентифікація отримувача може відбуватися кількома основними способами:
            - За банківськими реквізитами отримувача.
            - За номером платіжної картки отримувача.
            - За номером телефона отримувача.
            """)

    colD, colE, colF = st.columns(3)

    with colD:
        if st.button("Класифікація за місцем ініціації (фізичні точки)", key="4", use_container_width=True):
            modal_window("""
            Ініціювати переказ можна у фізичних точках, включаючи:
            - У відділенні банка.
            - Через платіжний термінал (наприклад, у звичайному магазині чи іншій торговій точці).
            """)

    with colE:
        if st.button("Класифікація за способами ініціації (дистанційні)", key="5", use_container_width=True):
            modal_window("""
            Дистанційні способи ініціації переказу охоплюють:
            - За допомогою систем дистанційного обслуговування (наприклад, мобільні застосунки чи інтернет-банкінг).
            - Через віртуальний термінал, що включає платежі через інтернет-сайти (зокрема через LiqPay, EasyPay, iPay.ua).
            - Використання платіжних сервісів, таких як Google Pay та Apple Pay.
            """)

    with colF:
        if st.button("Класифікація за формою коштів платника", key="6", use_container_width=True):
            modal_window("""
            Залежно від початкової форми коштів платника розрізняють:
            - Готівкова форма: Використовуються фізичні кошти, які платник вносить у касу або в платіжний термінал.
            - Безготівкова форма: Використовуються кошти, що знаходяться на банківському рахунку.
            """)

with tab2:
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Ранні передумови та зародження послуги", key="7", use_container_width=True):
            modal_window("""
            Хоча банки почали з’являтися ще у 9 сторіччі, послуга переказу коштів з’явилася пізніше, приблизно у 14–17 сторіччі, що було пов'язано з розвитком торгівлі та виробництва. В історії Стародавньої Греції згадується щось схоже на банки — це були міняйли, які обмінювали монети та брали кошти на зберігання, але вони ще не займалися переказами.
            """)

    with col2:
        if st.button("Ера паперових та телеграфних переказів", key="8", use_container_width=True):
            modal_window("""
            До 1871 року перекази здійснювалися виключно у паперовій формі. Ситуація змінилася у жовтні 1871 року, коли компанія Western Union почала надавати послугу переказів коштів через телеграф.
            """)

    with col3:
        if st.button("Розвиток у 20 столітті: карткові та міжбанківські системи", key="9", use_container_width=True):
            modal_window("""
            У 20 сторіччі, завдяки розвитку електроніки, почали з’являтися нові платіжні засоби та електронні процеси переказу коштів.
            - Виникли великі карткові платіжні системи, зокрема MasterCard, Visa та American Express.
            - У 1973 році у Бельгії була створена система SWIFT — міжнародна міжбанківська система для передавання інформації та здійснення платежів.
            - У 1998 році була створена платіжна система PayPal.
            """)

    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("Бурхливий розвиток 21 століття та нові екосистеми", key="10", use_container_width=True):
            modal_window("""
            У 21 сторіччі бурхливий розвиток технологій призвів до швидкого зростання різноманіття електронних платіжних інструментів. Було створено нові платіжні екосистеми:
            - Skrill (2001 рік).
            - Payoneer (2005 рік).
            - Stripe (2009 рік).
            - TransferWise (2010 рік).
            """)

    with col5:
        if st.button("Технологічні інновації 21 століття", key="11", use_container_width=True):
            modal_window("""
            Серед важливих технологічних інновацій 21 століття, що вплинули на перекази, є:
            - Поява віртуальних грошей у вигляді криптовалют.
            - Створення безлічі мобільних додатків для керування фінансами, пов'язане з розвитком мобільного зв’язку та смартфонів.
            - Поява переказів за QR-кодами.
            - Початок появи цифрових валют центральних банків.
            """)

    with col6:
        if st.button("Історія розвитку платіжної системи в Україні", key="12", use_container_width=True):
            modal_window("""
            - До 1993 року для переказу коштів в Україні використовувалися паперові чи телеграфні авізо.
            - У 1993 році була створена Система електронних платежів Національного банку України (СЕП).
            - З січня 1994 року СЕП стала основним засобом для переказу коштів в Україні.
            - СЕП модернізували у 2006 та 2017 роках.
            - З квітня 2023 року СЕП оновилася, перейшовши на міжнародний стандарт ISO 20022.
            - З 2017 року в Україні також почали створюватися фінтех-компанії, які пропонували банківські послуги із застосуванням сучасних технологій (наприклад, Monobank)
            """)

with tab3:
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("База сучасних переказів", key="13", use_container_width=True):
            modal_window("""
            Незважаючи на різноманіття варіантів, що пропонуються надавачами платіжних послуг, усі сучасні перекази базуються на певних технічних стандартах, які використовуються по всьому світу, з додаванням власних розробок.
            """)

    with col2:
        if st.button("Стандарт ISO 8583 (Карткові операції)", key="14", use_container_width=True):
            modal_window("""
            - Призначення: Стандарт для переказів коштів з використанням платіжних карток.
            - Історія: Перша версія була розроблена у 1987 році і з того часу отримала декілька оновлень.
            - Суть: На поточний час це основний стандарт для обміну фінансовою інформацією між різними терміналами та системами.
            - Переваги: Основні переваги використання ISO 8583 — компактність та швидкодія, які необхідні в карткових платіжних системах.
            - Зовнішній вигляд: Зовні виглядає як невеликий набір символів, який «розуміють» карткові пристрої та системи.
            """)
    with col3:
        if st.button("Стандарт ISO 20022 Ukraine (Внутрішньодержавні безготівкові перекази)", key="15",
                     use_container_width=True):
            modal_window("""
            - Призначення: Використовується для безготівкових переказів коштів за реквізитами в межах України.
            - Історія: Почав використовуватися в Україні у 2023 році після оновлення Системи електронних платежів НБУ.
            - Локалізація: Майже повністю відповідає міжнародному стандарту ISO 20022, але містить деякі локальні для України відмінності, пов’язані з українським законодавством.
            - Зовнішній вигляд: Зовні виглядає як великий документ формату XML.
            """)

    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("Стандарти для міжнародних переказів (ISO 20022 Swift та ISO 15022)", key="16",
                     use_container_width=True):
            modal_window("""
            - ISO 20022 Swift:
                - Призначення: Використовується для безготівкових міжнародних переказів коштів за реквізитами.
                - Історія: Затверджений у 2004 році.
                - Перспективи: Планується, що у майбутньому він буде використовуватися у всіх платіжних системах.
                - Використання SWIFT: З листопада 2025 року він використовується як основний стандарт для системи міжнародних переказів SWIFT.
                - Зовнішній вигляд: Виглядає як великий документ формату XML.
            - ISO 15022:
                - Призначення: Це застарілий стандарт для міжнародних переказів SWIFT.
                - Історія: Був основним стандартом у системі SWIFT з 1977 року по 2025 рік.
                - Виведення з експлуатації: З листопада 2025 року поступово стає застарілим і має бути виведений з експлуатації з 2026 року.
                - Зовнішній вигляд: Виглядає як текстовий документ, де кожен рядок починається з певного коду символів, що визначають тип інформації, вказаної в рядку.
            """)

    with col5:
        if st.button("Використання небанківських платіжних систем", key="17", use_container_width=True):
            modal_window("""
            В Україні існують та використовуються небанківські платіжні системи, такі як EasyPay, WayForPay, LiqPay, Portmone та інші. Вони надають платіжні шлюзи та API для своїх послуг. Будь-який варіант переказу коштів на поточний час використовує один із вищевказаних технічних стандартів або їх поєднання.
            """)

    with col6:
        if st.button("Приклади комбінацій стандартів у сучасних переказах", key="18", use_container_width=True):
            modal_window("""
            Сучасні перекази часто комбінують декілька стандартів для забезпечення повного циклу операції:
            1. Поповнення рахунку мобільного телефона за допомогою платіжної картки (у застосунку чи на сайті):
                - Спершу для списання коштів з картки застосовується ISO 8583.
                - Далі використовується один з платіжних шлюзів небанківських платіжних систем (наприклад, EasyPay) для зарахування коштів на особовий рахунок абонента.
                - На завершальному етапі, для фактичного зарахування коштів на рахунки мобільного оператора, виконується безготівковий переказ за допомогою стандарту ISO 20022 Ukraine.
            2. Зарахування заробітної плати працівнику:
                - У цьому випадку використовується лише один стандарт — ISO 20022 Ukraine — для перерахування коштів з рахунка роботодавця на рахунок працівника.
            3. Переказ коштів в іншу країну за допомогою платіжної картки (у застосунку банку):
                - Спочатку для списання коштів з картки застосовується ISO 8583.
                - Далі використовується стандарт ISO 20022 Swift для фактичного перерахування коштів на рахунок отримувача в іншій країні.
            """)
