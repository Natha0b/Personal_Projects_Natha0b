import { NextPage } from 'next';

interface PersonalInfo {
  name: string;
  profession: string;
  description: string;
  image: string;
}

const AboutPage: NextPage = () => {
  const personalInfo: PersonalInfo = {
    name: 'Nathaly Ortiz',
    profession: 'Student',
    description: 'I am in the process of becoming a software developer, I am passionate about technology, the new challenges and experiences that I am acquiring in this wonderful path of programming.☁️👩🏽‍💻',
    image: '/profile-image.jpg' // Ruta a tu imagen de perfil
  };

  return (
    <div>
      <h1>About Me</h1>
      <img src={personalInfo.image} alt="Profile Image" />
      <h2>{personalInfo.name}</h2>
      <h3>{personalInfo.profession}</h3>
      <p>{personalInfo.description}</p>
    </div>
  );
};

export default AboutPage;