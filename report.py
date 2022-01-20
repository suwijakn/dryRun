import streamlit as st
import pandas as pd
from itertools import cycle


def text(url):
     st.markdown(f'<p style="background-color:#F0F2F6;">{url}</p>', unsafe_allow_html=True)

def Display(i,q,path,sur):
    st.subheader(i + ') ' + q)
    list = df[df['FIRSTNAME'] == selected_row][q].values[0].split(',')
    list = [s.strip() for s in list]

    if list[0] == 'Not Answered':
        st.text('Not Answered')
        return

    images = []
    for image in list:
        images.append(path+ image + '.'+sur)

    cols = cycle(st.columns(5))
    for idx, filteredImage in enumerate(images):
        try:
            next(cols).image(filteredImage, width=200, caption=list[idx])
        except:
            if "idx" in locals():
                text(list[idx])
            if idx + 1 < len(images):
                print('yes')
                pass
            
st.set_page_config(layout="wide")
st.title("Respondents")
df = pd.read_csv('./Leads.csv')
df.index += 1 
st.write(df)

selected_row = st.selectbox('SELECT FIRSTNAME',['click here']+df.FIRSTNAME.to_list())
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

if selected_row != 'click here':
    st.title("รายบุคคล")
    st.subheader("ข้อมูลทั่วไป")
    col1, col2 = st.columns(2)
    with col1:
        st.write(df[df['FIRSTNAME'] == selected_row]['Date'].rename("วันที่ลงทะเบียน"))

    with col2:
        st.write(df[df['FIRSTNAME'] == selected_row]['FIRSTNAME'].rename("ชื่อ"))

    st.write(df[df['FIRSTNAME'] == selected_row]['Question Answered'].rename("จำนวนข้อที่ตอบคำถาม"))

    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.markdown("""<div style="text-align: center"> <h1>Lifestyle</h1> </div> """, unsafe_allow_html=True)

    # ในช่วง 2 สัปดาห์ โดยเฉลี่ยแล้วต้องทำกิจกรรมอะไรบ้าง และแต่ละกิจกรรมนั้นทำบ่อยแค่ไหน และใส่เสื้อผ้าประเภทอะไร
    st.subheader("1) ในช่วง 2 สัปดาห์ โดยเฉลี่ยแล้วต้องทำกิจกรรมอะไรบ้าง และแต่ละกิจกรรมนั้นทำบ่อยแค่ไหน และใส่เสื้อผ้าประเภทอะไร")
    #st.write(df[df['FIRSTNAME'] == selected_row]['ในช่วง 2 สัปดาห์ โดยเฉลี่ยแล้วต้องทำกิจกรรมอะไรบ้าง และแต่ละกิจกรรมนั้นทำบ่อยแค่ไหน และใส่เสื้อผ้าประเภทอะไร'].values[0])
    text(df[df['FIRSTNAME'] == selected_row]['ในช่วง 2 สัปดาห์ โดยเฉลี่ยแล้วต้องทำกิจกรรมอะไรบ้าง และแต่ละกิจกรรมนั้นทำบ่อยแค่ไหน และใส่เสื้อผ้าประเภทอะไร'].values[0])

    # เรียงลำดับความสำคัญ ของวัตถุประสงค์ ในการรับคำแนะนำ (1 = มากสุด) (8 = น้อยสุด)
    st.subheader("2) เรียงลำดับความสำคัญ ของวัตถุประสงค์ ในการรับคำแนะนำ (1 = มากสุด) (8 = น้อยสุด)")
    list = df[df['FIRSTNAME'] == selected_row]['เรียงลำดับความสำคัญ ของวัตถุประสงค์ ในการรับคำแนะนำ (1 = มากสุด) (8 = น้อยสุด)'].values[0].split(',')
    table = pd.DataFrame(range(1,8), columns=(['Rank']))
    table['Priority'] = list
    table.set_index(['Rank'],inplace=True)
    table.index.name = 'Rank'
    st.table(table)

    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.markdown("""<div style="text-align: center"> <h1>Personal Style</h1> </div> """, unsafe_allow_html=True)
    # เลือกเฉพาะรูปภาพที่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    st.subheader("3) เลือกเฉพาะรูปภาพที่ชอบ(เลือกได้มากกว่า 1 ข้อ)")
    list = df[df['FIRSTNAME'] == selected_row]['เลือกเฉพาะรูปภาพที่ชอบ(เลือกได้มากกว่า 1 ข้อ)'].values[0].split(',')
    list = [s.strip() for s in list]

    images = []
    for image in list:
        images.append('./images/Q3/'+ image + '.jpg')
    
    cols = cycle(st.columns(5))
    for idx, filteredImage in enumerate(images):
        next(cols).image(filteredImage, width=200, caption=list[idx])

    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.markdown("""<div style="text-align: center"> <h1>สิ่งที่ไม่ชอบและข้อจำกัด ทั่วๆไป</h1> </div> """, unsafe_allow_html=True)
    # ลาย (Pattern) แบบไหนบ้างที่ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    Display('4','ลาย (Pattern) แบบไหนบ้างที่ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)','./images/Q4/','png')

    # สี แบบไหนบ้างที่ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    Display('5','สี แบบไหนบ้างที่ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)','./images/Q5/','png')
        
    # วัสดุ (Material/Fabric) แบบไหนบ้างที่ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    st.subheader("6) วัสดุ (Material/Fabric) แบบไหนบ้างที่ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)")
    list = df[df['FIRSTNAME'] == selected_row]['วัสดุ (Material/Fabric) แบบไหนบ้างที่ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)'].values[0].split(',')
    table = pd.DataFrame(range(1,len(list)+1), columns=(['No.']))
    table['Material ที่ไม่ชอบ'] = list
    table.set_index(['No.'],inplace=True)
    table.index.name = 'No.'
    st.table(table)

    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.markdown("""<div style="text-align: center"> <h1>สิ่งที่ไม่ชอบและข้อจำกัด เสื้อ</h1> </div> """, unsafe_allow_html=True)
    # คอเสื้อ (Neckline) แบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    Display('7','คอเสื้อ (Neckline) แบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)','./images/Q7/','png')

    # แขนเสื้อ (Sleeve) แบบไหนบ้างที่คุณไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    Display('8','แขนเสื้อ (Sleeve) แบบไหนบ้างที่คุณไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)','./images/Q8/','png')

    # ชายเสื้อ (Waistlines) แบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    Display('9','ชายเสื้อ (Waistlines) แบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)','./images/Q9/','png')

    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.markdown("""<div style="text-align: center"> <h1>สิ่งที่ไม่ชอบและข้อจำกัด เดรสและกระโปรง</h1> </div> """, unsafe_allow_html=True)
    # ชุดเดรส (Waistlines) แบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    Display('10','ชุดเดรส (Waistlines) แบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)','./images/Q10/','png')

    # กระโปรงแบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    Display('11','กระโปรงแบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)','./images/Q11/','png')

    # ความยาวของ ชุดเดรสและกระโปรง แบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    Display('12','ความยาวของ ชุดเดรสและกระโปรง แบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)','./images/Q12/','png')

    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.markdown("""<div style="text-align: center"> <h1>สิ่งที่ไม่ชอบและข้อจำกัด กางเกง</h1> </div> """, unsafe_allow_html=True)
    # กางเกงแบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    Display('13','กางเกงแบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)','./images/Q13/','png')

    # ความยาวของ กางเกง แบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)
    Display('14','ความยาวของ กางเกง แบบไหนบ้างที่คุณ ไม่ชอบ(เลือกได้มากกว่า 1 ข้อ)','./images/Q14/','png')

    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.markdown("""<div style="text-align: center"> <h1>Body Shape</h1> </div> """, unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.subheader('15) รูปร่างของคุณเป็นแบบไหน')

        try:
            image = df[df['FIRSTNAME'] == selected_row]['รูปร่างของคุณเป็นแบบไหน'].values[0]
            st.image('./images/Q15/'+ image + '.png', width=200, caption=image)
        except:
            text(df[df['FIRSTNAME'] == selected_row]['รูปร่างของคุณเป็นแบบไหน'].values[0])
            
        
    with col4:
        st.subheader("16) นอกจากคำถามท่ีตอบมาทั้งหมดแล้วคุณสามารถให้ข้อมูลเพิ่มเติมกับทาง stylist เช่น สิ่งที่ไม่ชอบ หรือ ปัญหาเฉพาะเจาะจงที่อยากให้ทาง Stylist แนะนำ")
        text(df[df['FIRSTNAME'] == selected_row]['นอกจากคำถามท่ีตอบมาทั้งหมดแล้วคุณสามารถให้ข้อมูลเพิ่มเติมกับทาง stylist เช่น สิ่งที่ไม่ชอบ หรือ ปัญหาเฉพาะเจาะจงที่อยากให้ทาง Stylist แนะนำ'].values[0])
    
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("17) คุณสามารถ upload รูปภาพที่คิดว่าเป็นประโยชน์ต่อ Stylist ของเรา ได้ 1 รูป หากมีมากกว่า 1 รูป คุณสามารถส่งเพิ่มเติมได้ที่ Facebook Messenger")
        value = df[df['FIRSTNAME'] == selected_row]['คุณสามารถ upload รูปภาพที่คิดว่าเป็นประโยชน์ต่อ Stylist ของเรา ได้ 1 รูป หากมีมากกว่า 1 รูป คุณสามารถส่งเพิ่มเติมได้ที่ Facebook Messenger'].values[0]
        if value == 'Not Answered':
            text('Not Answered')
        else:
            st.image(value, width=200)
    
    with col6:
        st.subheader("18) ข้อเสนอแนะเพิ่มเติมสำหรับการทำแบบประเมินนี้")
        text(df[df['FIRSTNAME'] == selected_row]['ข้อเสนอแนะเพิ่มเติมสำหรับการทำแบบประเมินนี้'].values[0])

    #####

    

