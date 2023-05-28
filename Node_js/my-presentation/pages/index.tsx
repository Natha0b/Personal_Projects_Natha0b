import { NextPage } from 'next';
import Link from 'next/link';

const HomePage: NextPage = () => {
  return (
    <div>
      <h1>Welcome to My Personal Website!</h1>
      <Link href="/about">
        <a>Go to About Me</a>
      </Link>
    </div>
  );
};

export default HomePage;