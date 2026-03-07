from __future__ import annotations

import datetime as dt
import os
import struct
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
PRESENTATION_DIR = ROOT / "Presentation"
OUTPUT_PPTX = PRESENTATION_DIR / "HKU_Thesis_Defense.pptx"
OUTPUT_MD = PRESENTATION_DIR / "defense_ppt_outline.md"

NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_P = "http://schemas.openxmlformats.org/presentationml/2006/main"

SLIDE_W = 12192000
SLIDE_H = 6858000
EMU = 914400
TITLE_BOX = (int(0.55 * EMU), int(0.28 * EMU), int(12.0 * EMU), int(0.7 * EMU))
TEXT_BOX = (int(0.65 * EMU), int(1.15 * EMU), int(5.0 * EMU), int(5.75 * EMU))
IMAGE_BOX = (int(6.15 * EMU), int(1.15 * EMU), int(6.45 * EMU), int(5.7 * EMU))

SLIDES = [
    ("Tendon-Driven Mechanisms for Adaptive Robotic Grasping and Handheld Surgical Instruments",
     ["Yu Wang", "Supervisor: Prof. Peng Lu", "Department of Mechanical Engineering, HKU"],
     "Figures/overview_transparent.png",
     "Good morning, and thank you for attending my MPhil thesis defense. This thesis is mechanism-centered. Instead of presenting two unrelated devices, I study a common tendon-driven design framework and validate it through two embodiments: Lasso Gripper for adaptive grasping, and a handheld laparoscopic instrument for surgical manipulation."),
    ("Motivation",
     ["Narrow workspaces", "Fragile, irregular, or moving targets", "Low distal mass is required", "Tendon-driven systems offer compliance and remote actuation"],
     "Figures/surgical instrument.jpg",
     "Robotic manipulation becomes difficult when the workspace is constrained, when targets are fragile or irregular, and when the distal end must remain lightweight. These requirements appear in both general robotic grasping and minimally invasive surgery. Tendon-driven mechanisms are attractive because they transmit force through lightweight tensile elements and enable proximal actuation."),
    ("Research Gap",
     ["Surgical tools and adaptive grippers are often separate", "Most designs are application-driven", "A transferable tendon-driven framework is still missing"],
     "Figures/soft modular.png",
     "Existing literature contains many cable-driven surgical tools and many adaptive grippers, but these topics are usually studied in isolation. As a result, design knowledge remains application-specific. My thesis addresses this gap by extracting mechanism principles that can be transferred across domains."),
    ("Research Question",
     ["How can tendon-driven mechanisms be systematically designed", "to achieve adaptive, dexterous, and safe manipulation", "under limited space, low distal inertia, and compliant contact?"],
     "Figures/overview.png",
     "The central question of this thesis is how tendon-driven mechanisms can be systematically designed to achieve adaptive, dexterous, and safe manipulation under constraints of limited space, low distal inertia, and compliant contact. This question defines the whole thesis."),
    ("Main Contributions",
     ["Mechanism-level study of tendon-driven systems", "Lasso Gripper as the first embodiment", "Transferable design principles extracted", "Handheld surgical instrument as the second embodiment"],
     "Figures/overview_transparent.png",
     "The thesis makes four contributions. First, it studies tendon-driven systems at the mechanism level. Second, it develops Lasso Gripper as a novel adaptive grasping mechanism. Third, it extracts transferable design principles. Fourth, it translates those principles into a handheld laparoscopic instrument."),
    ("Thesis Roadmap",
     ["Problem definition", "Related work", "Lasso Gripper", "Extracted mechanism principles", "Surgical translation"],
     "Figures/overview_transparent.png",
     "This slide shows the roadmap of the thesis. I begin with the mechanism problem, then review related work. The first embodiment is Lasso Gripper, which is used to discover and validate mechanism principles. These principles are then transferred to the second embodiment, a handheld surgical instrument."),
    ("Related Work: Surgical Instruments",
     ["Cable-driven instruments improve distal dexterity", "Key issues: coupling, friction, hysteresis, weight", "The tradeoff between dexterity and usability remains open"],
     "Figures/trimmed.png",
     "On the surgical side, cable-driven instruments recover distal dexterity while keeping actuators away from the tip. However, this comes with coupling, friction, hysteresis, and practical weight penalties. Many studies optimize one part of the system, but fewer address the overall mechanism tradeoff between dexterity, tension control, and ergonomic usability."),
    ("Related Work: Adaptive Grasping",
     ["Soft and enveloping grippers improve shape adaptation", "Rigid grippers still struggle with fragile or oversized targets", "A mechanism with both capture range and controlled force is needed"],
     "Figures/8.png",
     "On the grasping side, soft and enveloping designs improve shape adaptability, but many systems sacrifice reach, force transmission, or controllability. Traditional rigid-finger grippers are less effective for fragile, oversized, or highly variable targets. This motivates a loop-based and tension-driven strategy."),
    ("Common Mechanism Principles",
     ["Tension management", "Proximal actuation", "Differential routing", "Compliant interaction", "Low distal inertia"],
     "Figures/overview.png",
     "These five principles unify the thesis. Tension management ensures predictable force transmission. Proximal actuation reduces distal mass. Differential routing enables compact multi-DOF behavior. Compliant interaction improves safety and adaptability."),
    ("Embodiment 1: Lasso Gripper Concept",
     ["Inspired by the lasso and the uurga", "Loop-based capture instead of point contact", "Adaptive capture region for uncertain targets"],
     "Figures/Figure1.png",
     "The first embodiment is Lasso Gripper. Its inspiration comes from traditional capture tools such as the lasso and the uurga. The key idea is to use a controllable string loop as the primary grasping structure, so that capture is achieved through tension-driven closure rather than rigid fingertip contact."),
    ("Lasso Gripper: Mechanical Design",
     ["Launch and retraction subsystems", "Friction-wheel-based string propulsion", "Spool mechanism for storage and recovery", "ESP32-based controller integration"],
     "Figures/overall_img.png",
     "This slide shows the hardware of Lasso Gripper. The system includes dedicated launch and retraction subsystems. Friction wheels propel the string to form the loop, while a spool handles storage and retraction. Mechanically, the design focuses on fast deployment, reliable recovery, and stable tension."),
    ("Lasso Gripper: Grasping Strategy",
     ["Point-cloud-based target understanding", "Caging-loop-based placement", "Controlled tightening with feedback"],
     "Figures/caging.png",
     "Grasping in Lasso Gripper combines mechanism and planning. The system identifies suitable loop placement based on point cloud information and caging principles. After loop positioning, tightening is coordinated with approach motion, while feedback regulates the capture process."),
    ("Lasso Gripper: Dynamics and Workspace",
     ["String-loop dynamics explain deployed behavior", "Workspace is estimated from loop geometry", "Modeling supports design and control"],
     "Figures/stringsim.png",
     "To move beyond demonstration, the loop behavior also needs to be understood analytically. This part of the thesis models the string dynamics and estimates the workspace associated with the deployed configuration. The analysis connects geometric behavior, launch conditions, and practical capture capability."),
    ("Lasso Gripper: Experimental Results",
     ["Static object capture", "Shape-adaptive grasping", "Oversized object handling", "Moving target capture"],
     "Figures/test1.png",
     "These experiments validate Lasso Gripper across a range of scenarios. It successfully captures animal figures, irregular objects, oversized balloons, and moving targets. Together, these demonstrations show that the loop-based mechanism offers both broad capture tolerance and gentle interaction."),
    ("Comparison with Conventional Grippers",
     ["Antipodal gripping concentrates stress", "Loop gripping distributes contact force", "Better for delicate and shape-variable targets"],
     "Figures/compare.png",
     "This comparison highlights why the mechanism matters. A conventional antipodal gripper applies concentrated stress to the target, which is problematic for delicate or highly deformable objects. In contrast, Lasso Gripper distributes contact through the loop."),
    ("Mechanism Insights from Lasso Gripper",
     ["Controlled tension improves repeatability", "Flexible contact improves tolerance to uncertainty", "Proximal actuation reduces distal complexity", "Differential routing is transferable"],
     "Figures/overview.png",
     "The key outcome of Lasso Gripper is not only a new end-effector. It also provides transferable mechanism insights. Controlled tension improves repeatability, flexible contact improves tolerance to uncertainty, and proximal actuation with differential routing can be reused beyond grasping."),
    ("Embodiment 2: Surgical Translation",
     ["Clinical constraints are much stricter", "Need distal dexterity without heavy distal hardware", "Need ergonomic balance and motion fidelity"],
     "Figures/surgical instrument.jpg",
     "The second embodiment tests the same mechanism framework in a more constrained setting. In minimally invasive surgery, the instrument must be slender, precise, ergonomic, and safe. This makes tendon-driven actuation especially relevant, because it allows actuation to remain proximal while producing multi-DOF motion at the tip."),
    ("Surgical Instrument: Design",
     ["Compact output actuation and input sensing", "Tension-preserving reel architecture", "Cable routing and tip design", "Quick-swap modular structure"],
     "Figures/Motor Arrangement.png",
     "This slide summarizes the architecture of the handheld surgical instrument. The design combines proximal actuation, compact motor arrangement, dedicated reel architecture, and precise cable routing. The reel is especially important because it preserves bidirectional tension and reduces slack accumulation."),
    ("Surgical Instrument: Control and Validation",
     ["Signal filtering plus closed-loop motor feedback", "Improved motion fidelity in a hand-held device", "Same mechanism principles under different constraints"],
     "Figures/input.png",
     "The control system combines signal filtering and closed-loop motor feedback to improve motion fidelity in a hand-held setting. At this point, the connection between the two embodiments becomes clear. Lasso Gripper validates adaptive interaction under uncertainty, while the surgical instrument validates dexterity and controllability under clinical constraints."),
    ("Conclusion and Future Work",
     ["A transferable tendon-driven framework is established", "Validated in grasping and surgical manipulation", "Future work: adaptive control, modular instruments, multi-loop grasping"],
     "Figures/overview_transparent.png",
     "In conclusion, this thesis shows that tendon-driven mechanisms can be systematically designed as a transferable framework for adaptive grasping, dexterous manipulation, and safe interaction. Lasso Gripper and the handheld surgical instrument are two embodiments of that same idea. Future work will further improve adaptive control, modularity, and loop-based grasping in dynamic environments."),
]


def image_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as f:
        header = f.read(32)
        if header.startswith(b"\x89PNG\r\n\x1a\n"):
            return struct.unpack(">II", header[16:24])
        if header[:2] == b"\xff\xd8":
            f.seek(2)
            while True:
                b = f.read(1)
                if not b:
                    break
                if b != b"\xff":
                    continue
                marker = f.read(1)
                while marker == b"\xff":
                    marker = f.read(1)
                if marker in {b"\xc0", b"\xc1", b"\xc2", b"\xc3", b"\xc5", b"\xc6", b"\xc7", b"\xc9", b"\xca", b"\xcb", b"\xcd", b"\xce", b"\xcf"}:
                    _len = struct.unpack(">H", f.read(2))[0]
                    f.read(1)
                    h, w = struct.unpack(">HH", f.read(4))
                    return w, h
                length = struct.unpack(">H", f.read(2))[0]
                f.seek(length - 2, os.SEEK_CUR)
    return 1600, 900


def fit_image(path: Path) -> tuple[int, int, int, int]:
    bx, by, bw, bh = IMAGE_BOX
    iw, ih = image_size(path)
    scale = min(bw / iw, bh / ih)
    w = int(iw * scale)
    h = int(ih * scale)
    return bx + (bw - w) // 2, by + (bh - h) // 2, w, h


def p_xml(text: str, *, bullet: bool, size: int) -> str:
    ppr = '<a:pPr/>' if not bullet else '<a:pPr marL="342900" indent="-228600"><a:buChar char="•"/></a:pPr>'
    return f'<a:p>{ppr}<a:r><a:rPr lang="en-US" sz="{size}"/><a:t>{escape(text)}</a:t></a:r><a:endParaRPr lang="en-US" sz="{size}"/></a:p>'


def text_shape(shape_id: int, name: str, box: tuple[int, int, int, int], paras: list[str]) -> str:
    x, y, w, h = box
    return f"""
    <p:sp>
      <p:nvSpPr><p:cNvPr id="{shape_id}" name="{escape(name)}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
      <p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln><a:noFill/></a:ln></p:spPr>
      <p:txBody><a:bodyPr wrap="square"><a:spAutoFit/></a:bodyPr><a:lstStyle/>{''.join(paras)}</p:txBody>
    </p:sp>"""


def pic_shape(shape_id: int, rel_id: str, box: tuple[int, int, int, int]) -> str:
    x, y, w, h = box
    return f"""
    <p:pic>
      <p:nvPicPr><p:cNvPr id="{shape_id}" name="Picture"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>
      <p:blipFill><a:blip r:embed="{rel_id}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>
      <p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr>
    </p:pic>"""


def slide_xml(title: str, bullets: list[str], has_img: bool, img_box: tuple[int, int, int, int] | None) -> str:
    title_paras = [f'<a:p><a:pPr/><a:r><a:rPr lang="en-US" sz="3000" b="1"><a:solidFill><a:srgbClr val="1F3A5F"/></a:solidFill></a:rPr><a:t>{escape(title)}</a:t></a:r><a:endParaRPr lang="en-US" sz="3000" b="1"/></a:p>']
    body_paras = [p_xml(b, bullet=True, size=2200) for b in bullets]
    pic = pic_shape(4, "rId2", img_box) if has_img and img_box else ""
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      {text_shape(2, "Title", TITLE_BOX, title_paras)}
      {text_shape(3, "Content", TEXT_BOX, body_paras)}
      {pic}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>"""


def slide_rels(media_name: str | None) -> str:
    rels = [
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>'
    ]
    if media_name:
        rels.append(f'<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/{media_name}"/>')
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + "".join(rels) + "</Relationships>"


def content_types() -> str:
    overrides = [
        '<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>',
        '<Override PartName="/ppt/presProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presProps+xml"/>',
        '<Override PartName="/ppt/viewProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"/>',
        '<Override PartName="/ppt/tableStyles.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"/>',
        '<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>',
        '<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>',
        '<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>',
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
        '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>',
    ]
    for i in range(1, len(SLIDES) + 1):
        overrides.append(f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>')
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Default Extension="png" ContentType="image/png"/><Default Extension="jpg" ContentType="image/jpeg"/><Default Extension="jpeg" ContentType="image/jpeg"/>' + "".join(overrides) + "</Types>"


def core_xml() -> str:
    now = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Tendon-Driven Mechanisms for Adaptive Robotic Grasping and Handheld Surgical Instruments</dc:title>
  <dc:creator>Yu Wang</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>"""


def app_xml() -> str:
    slides = len(SLIDES)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office PowerPoint</Application>
  <PresentationFormat>On-screen Show (16:9)</PresentationFormat>
  <Slides>{slides}</Slides>
  <Notes>0</Notes>
  <HiddenSlides>0</HiddenSlides>
  <MMClips>0</MMClips>
  <ScaleCrop>false</ScaleCrop>
  <HeadingPairs><vt:vector size="2" baseType="variant"><vt:variant><vt:lpstr>Theme</vt:lpstr></vt:variant><vt:variant><vt:i4>1</vt:i4></vt:variant></vt:vector></HeadingPairs>
  <TitlesOfParts><vt:vector size="1" baseType="lpstr"><vt:lpstr>Office Theme</vt:lpstr></vt:vector></TitlesOfParts>
  <Company>The University of Hong Kong</Company>
  <AppVersion>16.0000</AppVersion>
</Properties>"""


def presentation_xml() -> str:
    ids = [f'<p:sldId id="{255 + i}" r:id="rId{4 + i}"/>' for i in range(1, len(SLIDES) + 1)]
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}" saveSubsetFonts="1" autoCompressPictures="0">
  <p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>
  <p:sldIdLst>{''.join(ids)}</p:sldIdLst>
  <p:sldSz cx="{SLIDE_W}" cy="{SLIDE_H}" type="screen16x9"/>
  <p:notesSz cx="6858000" cy="9144000"/>
  <p:defaultTextStyle/>
</p:presentation>"""


def presentation_rels() -> str:
    rels = [
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>',
        '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/presProps" Target="presProps.xml"/>',
        '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/viewProps" Target="viewProps.xml"/>',
        '<Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/tableStyles" Target="tableStyles.xml"/>',
    ]
    for i in range(1, len(SLIDES) + 1):
        rels.append(f'<Relationship Id="rId{4 + i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>')
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + "".join(rels) + "</Relationships>"


def simple_xml(name: str) -> str:
    if name == "pres":
        return f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:presentationPr xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}" saveSubsetFonts="1" autoCompressPictures="0"/>'
    if name == "view":
        return f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:viewPr xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}" lastView="slideView" showComments="0"><p:normalViewPr/><p:slideViewPr><p:cSldViewPr snapToGrid="0" snapToObjects="1" showGuides="1"/></p:slideViewPr><p:notesTextViewPr/></p:viewPr>'
    return f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><a:tblStyleLst xmlns:a="{NS_A}" def="{{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}}"/>'


def master_xml() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}">
  <p:cSld name="Office Theme"><p:bg><p:bgPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:effectLst/></p:bgPr></p:bg><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst><p:sldLayoutId id="1" r:id="rId1"/></p:sldLayoutIdLst>
  <p:txStyles><p:titleStyle><a:lvl1pPr algn="l"/></p:titleStyle><p:bodyStyle><a:lvl1pPr marL="342900" indent="-228600"/></p:bodyStyle><p:otherStyle><a:lvl1pPr marL="342900" indent="-228600"/></p:otherStyle></p:txStyles>
</p:sldMaster>"""


def layout_xml() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}" type="blank" preserve="1">
  <p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>"""


def theme_xml() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="{NS_A}" name="Office Theme">
  <a:themeElements>
    <a:clrScheme name="Office">
      <a:dk1><a:srgbClr val="1F1F1F"/></a:dk1><a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="1F3A5F"/></a:dk2><a:lt2><a:srgbClr val="F3F6FA"/></a:lt2>
      <a:accent1><a:srgbClr val="2F5597"/></a:accent1><a:accent2><a:srgbClr val="70AD47"/></a:accent2>
      <a:accent3><a:srgbClr val="ED7D31"/></a:accent3><a:accent4><a:srgbClr val="FFC000"/></a:accent4>
      <a:accent5><a:srgbClr val="5B9BD5"/></a:accent5><a:accent6><a:srgbClr val="A5A5A5"/></a:accent6>
      <a:hlink><a:srgbClr val="0563C1"/></a:hlink><a:folHlink><a:srgbClr val="954F72"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="Office"><a:majorFont><a:latin typeface="Calibri Light"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont><a:minorFont><a:latin typeface="Calibri"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont></a:fontScheme>
    <a:fmtScheme name="Office"><a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst><a:lnStyleLst><a:ln w="6350"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst></a:fmtScheme>
  </a:themeElements>
  <a:objectDefaults/><a:extraClrSchemeLst/>
</a:theme>"""


def write_markdown() -> None:
    lines = [
        "# Thesis Defense PPT Outline",
        "",
        "Title: `Tendon-Driven Mechanisms for Adaptive Robotic Grasping and Handheld Surgical Instruments`",
        "",
        "Each slide below uses compressed bullet text suitable for PowerPoint.",
        "",
    ]
    for i, (title, bullets, image, script) in enumerate(SLIDES, start=1):
        lines += [f"## Slide {i}. {title}", "", f"Image: `{image}`", "", "Slide bullets:"]
        lines += [f"- {b}" for b in bullets]
        lines += ["", "Speaker script:", f"> {script}", ""]
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def build_pptx() -> None:
    media_cache: dict[str, str] = {}
    with zipfile.ZipFile(OUTPUT_PPTX, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types())
        zf.writestr(
            "_rels/.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>',
        )
        zf.writestr("docProps/core.xml", core_xml())
        zf.writestr("docProps/app.xml", app_xml())
        zf.writestr("ppt/presentation.xml", presentation_xml())
        zf.writestr("ppt/_rels/presentation.xml.rels", presentation_rels())
        zf.writestr("ppt/presProps.xml", simple_xml("pres"))
        zf.writestr("ppt/viewProps.xml", simple_xml("view"))
        zf.writestr("ppt/tableStyles.xml", simple_xml("table"))
        zf.writestr("ppt/theme/theme1.xml", theme_xml())
        zf.writestr("ppt/slideMasters/slideMaster1.xml", master_xml())
        zf.writestr(
            "ppt/slideMasters/_rels/slideMaster1.xml.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/></Relationships>',
        )
        zf.writestr("ppt/slideLayouts/slideLayout1.xml", layout_xml())
        zf.writestr(
            "ppt/slideLayouts/_rels/slideLayout1.xml.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/></Relationships>',
        )

        for i, (title, bullets, image, _script) in enumerate(SLIDES, start=1):
            media_name = None
            img_box = None
            img_path = ROOT / image
            if img_path.exists():
                if image not in media_cache:
                    media_name = f"image{len(media_cache) + 1}{img_path.suffix.lower()}"
                    media_cache[image] = media_name
                    zf.write(img_path, f"ppt/media/{media_name}")
                media_name = media_cache[image]
                img_box = fit_image(img_path)
            zf.writestr(f"ppt/slides/slide{i}.xml", slide_xml(title, bullets, media_name is not None, img_box))
            zf.writestr(f"ppt/slides/_rels/slide{i}.xml.rels", slide_rels(media_name))


if __name__ == "__main__":
    PRESENTATION_DIR.mkdir(parents=True, exist_ok=True)
    write_markdown()
    build_pptx()
    print(f"Wrote {OUTPUT_MD}")
    print(f"Wrote {OUTPUT_PPTX}")
