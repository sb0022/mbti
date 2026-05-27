
import streamlit as st
import time

# 1. 페이지 기본 설정 (가장 먼저 실행되어야 합니다)
st.set_page_config(
    page_title="MBTI 찰떡 포켓몬 찾기",
    page_icon="✨",
    layout="centered"
)

# 2. MBTI별 포켓몬 데이터베이스 (이미지 링크 포함)
pokemon_db = {
    "INFP": {
        "name": "뮤 (Mew)",
        "emoji": "🦄",
        "desc": "공상하기를 좋아하고 마음이 따뜻한 당신은 신비롭고 순수한 '뮤'와 닮았어요! 혼자만의 시간을 소중히 여기며 언제나 평화를 바랍니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png"
    },
    "ENFP": {
        "name": "피카츄 (Pikachu)",
        "emoji": "⚡",
        "desc": "언제나 에너지가 넘치고 통통 튀는 당신은 모두의 사랑을 받는 '피카츄' 그 자체! 호기심이 많고 주변 사람들에게 밝은 에너지를 전파해요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
    },
    "INFJ": {
        "name": "가디안 (Gardevoir)",
        "emoji": "🔮",
        "desc": "통찰력이 뛰어나고 세심한 당신은 트레이너를 온 힘을 다해 지키는 '가디안'과 어울려요. 깊은 공감 능력과 신비로운 분위기를 가지고 있습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"
    },
    "ENFJ": {
        "name": "토게키스 (Togekiss)",
        "emoji": "🕊️",
        "desc": "주변에 행복과 평화를 전파하는 다정한 리더인 당신은 '토게키스'와 똑 닮았어요! 사람들을 격려하고 이끄는 데 천부적인 재능이 있습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png"
    },
    "INTJ": {
        "name": "뮤츠 (Mewtwo)",
        "emoji": "🧠",
        "desc": "전략적이고 독립적이며 완벽을 추구하는 당신은 냉철한 천재 '뮤츠'와 닮았네요! 복잡한 문제를 해결하는 것을 좋아하고 주관이 뚜렷합니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png"
    },
    "ENTJ": {
        "name": "리자몽 (Charizard)",
        "emoji": "🔥",
        "desc": "강력한 카리스마와 당당한 자신감을 가진 당신은 열정적인 리더 '리자몽'입니다! 목표를 향해 거침없이 나아가며 팀을 승리로 이끕니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"
    },
    "INTP": {
        "name": "폴리곤 (Porygon)",
        "emoji": "💻",
        "desc": "논리적이고 호기심이 많은 분석가인 당신은 데이터로 이루어진 포켓몬 '폴리곤'과 어울려요! 새로운 지식을 탐구하고 시스템을 이해하는 것을 즐깁니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/137.png"
    },
    "ENTP": {
        "name": "팬텀 (Gengar)",
        "emoji": "😈",
        "desc": "위트 있고 장난기를 좋아하는 재치 만점 당신은 '팬텀'과 찰떡궁합! 고정관념을 깨는 것을 좋아하고 토론과 말싸움에서 절대 지지 않아요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png"
    },
    "ISFP": {
        "name": "이브이 (Eevee)",
        "emoji": "🦊",
        "desc": "예술적 감각이 뛰어나고 유연한 사고를 가진 당신은 무한한 가능성의 '이브이'입니다! 갈등을 싫어하며, 상황에 맞게 자신을 변화시킬 줄 압니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"
    },
    "ESFP": {
        "name": "푸린 (Jigglypuff)",
        "emoji": "🎤",
        "desc": "어디서나 주목받는 분위기 메이커인 당신은 스타성이 넘치는 '푸린'과 닮았어요! 흥이 많고 사람들과 어울려 노는 것을 가장 좋아합니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"
    },
    "ISTP": {
        "name": "개굴닌자 (Greninja)",
        "emoji": "🥷",
        "desc": "말보다는 행동! 상황 적응력이 뛰어나고 손재주가 좋은 당신은 시크하고 민첩한 '개굴닌자'입니다. 효율성을 중요하게 생각하는 쿨한 성격이에요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/658.png"
    },
    "ESTP": {
        "name": "루카리오 (Lucario)",
        "emoji": "👊",
        "desc": "스릴을 즐기고 에너제틱한 당신은 실전 감각이 뛰어난 '루카리오'와 어울려요! 몸으로 부딪히며 배우는 것을 좋아하고 위기 대처 능력이 만점입니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png"
    },
    "ISFJ": {
        "name": "치코리타 (Chikorita)",
        "emoji": "🍃",
        "desc": "책임감이 강하고 주변 사람들을 헌신적으로 챙기는 당신은 다정한 '치코리타'와 닮았어요! 차분하고 안정적인 환경을 만들며 모두에게 편안함을 줍니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/152.png"
    },
    "ESFJ": {
        "name": "해피너스 (Blissey)",
        "emoji": "🥚",
        "desc": "타인의 행복이 곧 나의 행복! 친절하고 사교적인 당신은 모두를 치유해주는 '해피너스'입니다. 리액션이 좋아서 주변에 늘 사람이 모여요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png"
    },
    "ISTJ": {
        "name": "꼬부기 (Squirtle)",
        "emoji": "🐢",
        "desc": "원칙을 지키고 매사에 신중하며 철저한 당신은 모범생 '꼬부기'를 닮았군요! 약속을 잘 지키고 맡은 바 임무를 묵묵히 완수하는 신뢰감 100%의 사람입니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png"
    },
    "ESTJ": {
        "name": "윈디 (Arcanine)",
        "emoji": "🦁",
        "desc": "체계적이고 리더십이 있으며 의리가 넘치는 당신은 든든한 '윈디'와 같습니다! 공정함을 중요시하고 규칙에 따라 일을 완벽하게 처리합니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png"
    }
}

# 3. UI 꾸미기
st.title("🐾 나의 MBTI 찰떡 포켓몬은?")
st.write("당신의 MBTI를 선택하고, 영혼의 파트너 포켓몬을 만나보세요! ✨")
st.markdown("---")

# MBTI 선택 박스 (알파벳 정렬 순)
mbti_list = sorted(list(pokemon_db.keys()))
selected_mbti = st.selectbox("🎯 당신의 MBTI를 선택하세요:", mbti_list, index=None, placeholder="여기 치고 선택하거나 골라보세요 👀")

if selected_mbti:
    # 귀여운 로딩 효과
    with st.spinner('🔮 당신의 성향을 분석해서 포켓몬을 소환하는 중...'):
        time.sleep(1.5)  # 1.5초 대기 시각 효과
    
    # 선택된 포켓몬 데이터 가져오기
    pokemon = pokemon_db[selected_mbti]
    
    # 결과 화면 구성
    st.balloons() # 축하 풍선 팡팡!
    
    st.success(def_text := f"✨ {selected_mbti}인 당신에게 딱 맞는 포켓몬은... ✨")
    
    # 2단 레이아웃 분할 (왼쪽: 이미지, 오른쪽: 설명)
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.image(pokemon["image"], use_container_width=True)
        
    with col2:
        st.subheader(f"{pokemon['emoji']} {pokemon['name']}")
        st.write("")
        st.info(pokemon["desc"])
        
    st.markdown("---")
    st.caption("💡 친구들에게 링크를 공유해서 서로 어떤 포켓몬이 나왔는지 비교해보세요!")
