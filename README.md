# LikeLion

<!DOCTYPE html>
<meta charset="utf-8">
<html>

<head>
    <link rel="stylesheet" href="codelion.css">
    <title> About Son </title>
</head>

<body>
    <div class="first-box">
        <h1>손민혁</h1>
        <p class="backend"> 백엔드 개발자</p>
    </div>

    
    <section class="intro-box">
        <h2>ABOUT ME</h2>
        <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus hic laboriosam, velit recusandae perspiciatis minus laudantium aliquid. Suscipit animi dolor enim corrupti dolorum cupiditate praesentium, pariatur a laboriosam facilis eveniet?</p>
    </section>
    


    <section class="experience-box">
        <h2>EXPERIENCE</h2>
            <div>
                <p class="title-text">Aweosome Programming Company</p>
                <p class="year-text">2022 - Now</p>
                <p class="desc-text">Front-End Web Developer</p>
                <p class="desc-subtext">HTML/CSS, JS, React etc.</p>
            </div>

            <div>
                <p class="title-text">KINTEX</p>
                <p class="year-text">2020 - 2021</p>
                <p class="desc-text">UX/UI Designer</p>
                <p class="desc-subtext">Web design</p>
            </div>

            <div>
                <p class="title-text">Freelance Work</p>
                <p class="year-text">2018 - 2019</p>
                <p class="desc-text">Graphic Designer</p>
                <p class="desc-subtext">Graphic Design, Editorial Design</p>
            </div>
    </section>

<!-- 하나 박스를 완성해두고 나머지를 복붙하는 게 더 효율적이겠다. -->
<!-- class는 같은 이름으로 여러 군데 써도 상관 없구나. -->
<!-- float: right; 한 번 해서는 기억하기 힘들 것 같다. 여러 번 만들면서 이런 게 있구나 하고 몸으로 익히자 -->
<!-- overflow: hidden; -> 이거 다시 공부하기 -->
<!-- 테두리속성 border: 3px 실선 black 0.3; 이것도 다시 공부하자 -->

    <section class="activity-box">
        <h2>ACTIVITIES</h2>
            <div>
                <p class="title-text">Front-End Web Developer Forum Volunteer</p>
                <p class="year-text">2019 - 2020</p>
                <p class="desc-text">Application Page Development</p>
                <p class="desc-subtext">Lorem ipsum dolor sit amet..</p>
            </div>

            <div>
                <p class="title-text">LIKELION SEOUL</p>
                <p class="year-text">2017 - 2018</p>
                <p class="desc-text">Teacher in Musta University</p>
                <p class="desc-subtext">Lorem ipsum dolor sit amet..</p>
            </div>

            <div>
                <p class="title-text">Open Source Committer</p>
                <p class="year-text">2011 -2013</p>
                <p class="desc-text">Angular JS</p>
                <p class="desc-subtext">Lorem ipsum dolor sit amet..</p>
            </div>
    </section>

    <section class="education-box">
        <h2>EDUCATION</h2>
            <div>
                <p class="title-text">Musta University</p>
                <p class="year-text">2008 - 2012</p>
                <p class="desc-text">Computer Science and Engineering</p>
            </div>

            <div>
                <p class="title-text">Musta High School</p>
                <p class="year-text">2006 - 2008</p>
                <p class="desc-text">Visual Communication Design</p>
            </div>

            <div>
                <p class="title-text">Online Programming Academy</p>
                <p class="year-text">2006 -2007</p>
                <p class="desc-text">Python Course</p>
            </div>
    </section>

    <section class="awards-box">
        <h2>AWARDS</h2>
            <div>
                <p class="title-text">LIKELION SEOUL</p>
                <p class="year-text">2018</p>
                <p class="desc-text">Best Developer Award</p>
            </div>
    </section>


 <!-- 왜 class="insta-image"에 margin, padding right를 0px로 해도 오른쪽에 여백이 남지.. -->
    <div class="sns-box">
        <a href="https://www.instagram.com/"><img class = "insta-image" src="insta.jpg"></a>
    </div>
    
    <footer>
        <p>Copyright CODE LION ALL rights reserved.</p>
    </footer>
       
</body>


</html>



# 여기서부터는 CSS
@import url('https://fonts.googleapis.com/css?family=Montserrat:100,200,300,400,500,600,700,800&display=swap');

* {
    font-family: 'Montserrat';
}


body, h1, h2 {
    margin: 0px;
    padding: 0px;
    margin-right: 15px;
}

h1 {
   font-size: 45px; 
   font-style: italic;
   padding-top: 30px;
   padding-bottom: 0px;
}

h2 {
    border-bottom: 1px solid #c0c0b8;
    font-size: 24px;
    color: #282828;
    font-weight: lighter;
    margin-bottom: 15px;
    padding-bottom: 7px;
    margin-top: 30px;

}

.first-box {
    text-align: right;
    margin-right: 60px;
}

.backend {
    font-size: 25px;
    padding-top: 0px;
    margin-top: 15px;
    color: #76766A;
    font-weight: bold
}

.title-text {
    font-weight: bold;
    font-size: 16px;
    margin-top: 30px;
}

.year-text {
    font-size: 15px;
    font-weight: bold;
    color: #282828;
    float: right;
}

.desc-subtext {
    padding-left: 15px;
    font-size: 14px;
}

.sns-box {
    text-align: right;
    padding-right: 0px;
    margin-right: 0px;
}
.insta-image {
    width: 45px;
    height: 45px;
    margin-top: 20px;
    margin-right: 0px;
    padding-right: 0px;
}

footer {
    text-align: center;
    margin-top: 50px;
    background-color: #1e1e1e;
    color: #919191;
    padding-top: 30px;
    padding-bottom: 30px;
  
}