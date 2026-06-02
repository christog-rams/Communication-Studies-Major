import streamlit as st

st.set_page_config(page_title="CSU Comm Studies Tracker", page_icon="🎓", layout="wide")

# ── Degree data ────────────────────────────────────────────────────────────────

SECTIONS = [
    {
        "id": "fr", "year": "Freshman", "color": "#534AB7",
        "groups": [
            { "label": "Required courses", "courses": [
                {"code": "CO 150",    "name": "College Composition",                               "aucc": "1A",  "cr": 3},
                {"code": "SPCM 100",  "name": "Communication and Popular Culture",                 "aucc": "3B",  "cr": 3},
                {"code": "SPCM 130",  "name": "Foundations of Human Communication",                "aucc": "3C",  "cr": 3},
                {"code": "SPCM 200",  "name": "Public Speaking",                                   "aucc": "",    "cr": 3},
                {"code": "AUCC 1B",   "name": "AUCC 1B requirement",                               "aucc": "1B",  "cr": 3},
                {"code": "AUCC 1C",   "name": "AUCC 1C requirement",                               "aucc": "1C",  "cr": 3},
                {"code": "AUCC 3A",   "name": "Biological & Physical Sciences (two courses)",      "aucc": "3A",  "cr": 7},
                {"code": "Electives", "name": "Free electives",                                    "aucc": "",    "cr": 6},
            ]},
        ],
    },
    {
        "id": "so", "year": "Sophomore", "color": "#0F6E56",
        "groups": [
            { "label": "Required SPCM courses", "courses": [
                {"code": "SPCM 201", "name": "Introduction to Rhetoric",  "aucc": "3B", "cr": 3},
                {"code": "SPCM 207", "name": "Public Argumentation",       "aucc": "",   "cr": 3},
            ]},
            { "label": "Advanced writing — choose one (AUCC 2)", "choice": True, "courses": [
                {"code": "CO 300",  "name": "Writing Arguments",                               "aucc": "2", "cr": 3},
                {"code": "CO 301A", "name": "Writing in the Disciplines: Arts and Humanities", "aucc": "2", "cr": 3},
                {"code": "CO 301B", "name": "Writing in the Disciplines: Sciences",            "aucc": "2", "cr": 3},
                {"code": "CO 301C", "name": "Writing in the Disciplines: Social Sciences",     "aucc": "2", "cr": 3},
                {"code": "CO 301D", "name": "Writing in the Disciplines: Education",           "aucc": "2", "cr": 3},
            ]},
            { "label": "Distribution requirements", "courses": [
                {"code": "AUCC 3D",  "name": "Historical Perspectives",                                             "aucc": "3D", "cr": 3},
                {"code": "Arts/Hum", "name": "Additional Arts & Humanities (6 cr — ART, D, E, ETST, L***, MU, PHIL, TH, WS)", "aucc": "", "cr": 6},
                {"code": "History",  "name": "Additional History — HIST subject code (6 cr)",                       "aucc": "",   "cr": 6},
                {"code": "Soc/Beh",  "name": "Additional Social & Behavioral Sciences (6 cr)",                      "aucc": "",   "cr": 6},
            ]},
        ],
    },
    {
        "id": "jr", "year": "Junior", "color": "#185FA5",
        "groups": [
            { "label": "SPCM electives (15 of 24 total required)", "courses": [
                {"code": "SPCM ***", "name": "Communication Studies elective", "aucc": "", "cr": 3},
                {"code": "SPCM ***", "name": "Communication Studies elective", "aucc": "", "cr": 3},
                {"code": "SPCM ***", "name": "Communication Studies elective", "aucc": "", "cr": 3},
                {"code": "SPCM ***", "name": "Communication Studies elective", "aucc": "", "cr": 3},
                {"code": "SPCM ***", "name": "Communication Studies elective", "aucc": "", "cr": 3},
            ]},
            { "label": "Minor or interdisciplinary minor (15 of 21 cr)", "minor": True, "courses": [
                {"code": "Minor", "name": "", "aucc": "", "cr": 3},
                {"code": "Minor", "name": "", "aucc": "", "cr": 3},
                {"code": "Minor", "name": "", "aucc": "", "cr": 3},
                {"code": "Minor", "name": "", "aucc": "", "cr": 3},
                {"code": "Minor", "name": "", "aucc": "", "cr": 3},
            ]},
        ],
    },
    {
        "id": "sr", "year": "Senior", "color": "#BA7517",
        "groups": [
            { "label": "Capstone (required)", "courses": [
                {"code": "SPCM 479", "name": "Communication Studies Capstone", "aucc": "4C", "cr": 3},
            ]},
            { "label": "Upper-division SPCM — choose one (AUCC 4A/4B)", "choice": True, "courses": [
                {"code": "SPCM 311",  "name": "Historical Speeches on American Issues",      "aucc": "4A/4B", "cr": 3},
                {"code": "SPCM 341",  "name": "Evaluating Contemporary Television",          "aucc": "4A/4B", "cr": 3},
                {"code": "SPCM 342",  "name": "Critical Media Studies",                      "aucc": "4A/4B", "cr": 3},
                {"code": "SPCM 350",  "name": "Evaluating Contemporary Film",                "aucc": "4A/4B", "cr": 3},
                {"code": "SPCM 354A", "name": "Film History: International",                 "aucc": "4A/4B", "cr": 3},
                {"code": "SPCM 354B", "name": "Film History: United States",                 "aucc": "4A/4B", "cr": 3},
                {"code": "SPCM 411",  "name": "Contemporary Speeches on American Issues",    "aucc": "4A/4B", "cr": 3},
                {"code": "SPCM 412",  "name": "Rhetorical Criticism",                        "aucc": "4A/4B", "cr": 3},
                {"code": "SPCM 420",  "name": "Political Communication",                     "aucc": "4A/4B", "cr": 3},
                {"code": "SPCM 433",  "name": "Organizational Communication",                "aucc": "4A/4B", "cr": 3},
                {"code": "SPCM 434",  "name": "International & Intercultural Communication", "aucc": "4A/4B", "cr": 3},
            ]},
            { "label": "Remaining SPCM electives (9 cr)", "courses": [
                {"code": "SPCM ***", "name": "Communication Studies elective", "aucc": "", "cr": 3},
                {"code": "SPCM ***", "name": "Communication Studies elective", "aucc": "", "cr": 3},
                {"code": "SPCM ***", "name": "Communication Studies elective", "aucc": "", "cr": 3},
            ]},
            { "label": "Remaining minor (6 cr)", "minor": True, "courses": [
                {"code": "Minor", "name": "", "aucc": "", "cr": 3},
                {"code": "Minor", "name": "", "aucc": "", "cr": 3},
            ]},
            { "label": "Free electives", "courses": [
                {"code": "Elective", "name": "Free elective credits", "aucc": "", "cr": 8},
            ]},
        ],
    },
]

# ── Session state init ─────────────────────────────────────────────────────────

def init_state():
    if "student_name" not in st.session_state:
        st.session_state.student_name = ""
    if "minor_names" not in st.session_state:
        st.session_state.minor_names = {}
    if "extra_courses" not in st.session_state:
        st.session_state.extra_courses = {}

init_state()

# ── Helpers ────────────────────────────────────────────────────────────────────

def chk_key(sec_id, gi, ci):
    return f"chk_{sec_id}__{gi}__{ci}"

def is_checked(sec_id, gi, ci):
    return st.session_state.get(chk_key(sec_id, gi, ci), False)

def earned_credits():
    total = 0
    for sec in SECTIONS:
        for gi, g in enumerate(sec["groups"]):
            for ci, c in enumerate(g["courses"]):
                if is_checked(sec["id"], gi, ci):
                    total += c["cr"]
        for extra in st.session_state.extra_courses.get(sec["id"], []):
            if st.session_state.get(f"extchk_{sec['id']}_{extra['_ei']}", False):
                total += extra["cr"]
    return total

def spcm_credits():
    total = 0
    for sec in SECTIONS:
        for gi, g in enumerate(sec["groups"]):
            for ci, c in enumerate(g["courses"]):
                if c["code"].startswith("SPCM") and is_checked(sec["id"], gi, ci):
                    total += c["cr"]
    return total

# ── Styling ────────────────────────────────────────────────────────────────────

st.markdown("""
<style>
    .block-container { padding-top: 1.5rem; }
    .metric-card { background: #f7f7f5; border-radius: 10px; padding: 0.75rem 1rem; }
    .metric-label { font-size: 11px; color: #888; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 2px; }
    .metric-value { font-size: 26px; font-weight: 600; color: #1a1a1a; }
    .metric-sub { font-size: 11px; color: #aaa; }
    .aucc-pill { display: inline-block; font-size: 10px; background: #f0f0ec; color: #888; border-radius: 99px; padding: 1px 7px; margin-left: 6px; }
    .choice-note { font-size: 11px; color: #999; font-style: italic; margin-top: -8px; margin-bottom: 8px; padding-left: 28px; }
    .section-divider { border: none; border-top: 1px solid #eee; margin: 8px 0; }
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────

st.markdown("### 🎓 B.A. Communication Studies")
st.caption("Colorado State University · 2025–2026 Catalog")

name_col, _ = st.columns([2, 3])
with name_col:
    st.session_state.student_name = st.text_input(
        "Student name",
        value=st.session_state.student_name,
        placeholder="Enter student name",
    )
    if st.session_state.student_name:
        st.caption(f"Advising plan for **{st.session_state.student_name}**")

st.divider()

# ── Metrics (computed AFTER all widget keys exist in session_state) ─────────────

earned    = earned_credits()
remaining = max(0, 120 - earned)
pct       = min(100, round(earned / 120 * 100))
spcm      = spcm_credits()

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Credits earned</div><div class="metric-value">{earned}</div><div class="metric-sub">of 120 required</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Progress</div><div class="metric-value">{pct}%</div><div class="metric-sub">toward degree</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown(f'<div class="metric-card"><div class="metric-label">SPCM credits</div><div class="metric-value">{spcm}</div><div class="metric-sub">of 24+ required</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Remaining</div><div class="metric-value">{remaining}</div><div class="metric-sub">credits to complete</div></div>', unsafe_allow_html=True)

st.progress(pct / 100)
st.markdown("<br>", unsafe_allow_html=True)

# ── Year sections ──────────────────────────────────────────────────────────────

YEAR_COLORS = {"Freshman": "#534AB7", "Sophomore": "#0F6E56", "Junior": "#185FA5", "Senior": "#BA7517"}

for sec in SECTIONS:
    sec_id = sec["id"]
    year   = sec["year"]

    done_count  = sum(is_checked(sec_id, gi, ci)
                      for gi, g in enumerate(sec["groups"])
                      for ci in range(len(g["courses"])))
    total_count = sum(len(g["courses"]) for g in sec["groups"])
    badge = "Complete" if done_count == total_count else ("In progress" if done_count > 0 else "Not started")

    with st.expander(f"**{year} year** — {done_count}/{total_count} complete · {badge}", expanded=(year == "Freshman")):

        for gi, group in enumerate(sec["groups"]):
            is_choice = group.get("choice", False)
            is_minor  = group.get("minor", False)

            st.markdown(f"**{group['label']}**")
            if is_choice:
                st.markdown('<div class="choice-note">Select one from this group</div>', unsafe_allow_html=True)

            for ci, course in enumerate(group["courses"]):
                key = chk_key(sec_id, gi, ci)
                checked = st.session_state.get(key, False)

                col_chk, col_code, col_name, col_aucc, col_cr = st.columns([0.5, 1, 5, 1, 0.7])

                with col_chk:
                    st.checkbox("", key=key, label_visibility="collapsed")

                with col_code:
                    st.markdown(f"<span style='font-size:11px;font-family:monospace;color:#888'>{course['code']}</span>", unsafe_allow_html=True)

                with col_name:
                    if is_minor:
                        mkey = f"minor_{key}"
                        new_name = st.text_input("", value=st.session_state.minor_names.get(mkey, course["name"]),
                                                  placeholder="Enter minor course name",
                                                  key=f"minput_{key}", label_visibility="collapsed")
                        st.session_state.minor_names[mkey] = new_name
                    else:
                        style = "text-decoration:line-through;color:#aaa;" if checked else ""
                        st.markdown(f"<span style='font-size:13px;{style}'>{course['name']}</span>", unsafe_allow_html=True)

                with col_aucc:
                    if course["aucc"]:
                        st.markdown(f"<span class='aucc-pill'>{course['aucc']}</span>", unsafe_allow_html=True)

                with col_cr:
                    st.markdown(f"<span style='font-size:12px;color:#aaa'>{course['cr']} cr</span>", unsafe_allow_html=True)

            if is_minor:
                with st.expander("➕ Add minor course", expanded=False):
                    mc1, mc2, mc3, mc4 = st.columns([1, 3, 0.8, 1])
                    with mc1:
                        m_code = st.text_input("Code", placeholder="e.g. PSY 301", key=f"mc_{sec_id}_{gi}")
                    with mc2:
                        m_name = st.text_input("Course name", placeholder="Course name", key=f"mn_{sec_id}_{gi}")
                    with mc3:
                        m_cr = st.number_input("Cr", min_value=1, max_value=6, value=3, key=f"mcr_{sec_id}_{gi}")
                    with mc4:
                        st.markdown("<br>", unsafe_allow_html=True)
                        if st.button("Add", key=f"madd_{sec_id}_{gi}"):
                            if m_name:
                                extras = st.session_state.extra_courses.setdefault(sec_id, [])
                                ei = len(extras)
                                extras.append({"code": m_code or "Minor", "name": m_name, "cr": m_cr, "_ei": ei})
                                st.rerun()

            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

        # Extra added courses
        extras = st.session_state.extra_courses.get(sec_id, [])
        if extras:
            st.markdown("**Added courses**")
            to_remove = []
            for extra in extras:
                ei = extra["_ei"]
                ec1, ec2, ec3, ec4 = st.columns([0.5, 1.5, 5, 1])
                with ec1:
                    st.checkbox("", key=f"extchk_{sec_id}_{ei}", label_visibility="collapsed")
                with ec2:
                    st.markdown(f"<span style='font-size:11px;font-family:monospace;color:#888'>{extra['code']}</span>", unsafe_allow_html=True)
                with ec3:
                    done = st.session_state.get(f"extchk_{sec_id}_{ei}", False)
                    style = "text-decoration:line-through;color:#aaa;" if done else ""
                    st.markdown(f"<span style='font-size:13px;{style}'>{extra['name']}</span>", unsafe_allow_html=True)
                with ec4:
                    if st.button("✕", key=f"del_{sec_id}_{ei}"):
                        to_remove.append(ei)
            if to_remove:
                st.session_state.extra_courses[sec_id] = [e for e in extras if e["_ei"] not in to_remove]
                st.rerun()
            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

        # Add any course
        with st.expander("➕ Add a course to this year", expanded=False):
            a1, a2, a3, a4 = st.columns([1, 3, 0.8, 1])
            with a1:
                a_code = st.text_input("Code", placeholder="e.g. SPCM 310", key=f"ac_{sec_id}")
            with a2:
                a_name = st.text_input("Course name", placeholder="Course name", key=f"an_{sec_id}")
            with a3:
                a_cr = st.number_input("Cr", min_value=1, max_value=6, value=3, key=f"acr_{sec_id}")
            with a4:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("Add", key=f"aadd_{sec_id}"):
                    if a_name:
                        extras = st.session_state.extra_courses.setdefault(sec_id, [])
                        ei = len(extras)
                        extras.append({"code": a_code or "—", "name": a_name, "cr": a_cr, "_ei": ei})
                        st.rerun()

# ── Footer ─────────────────────────────────────────────────────────────────────

st.divider()
st.caption("CSU Communication Studies · 2025–2026 Catalog · 120 credits required · at least 42 upper-division (300–400 level)")
