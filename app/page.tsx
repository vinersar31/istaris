import Link from 'next/link';
import Hero from './components/Hero';
import Features from './components/Features';
import Team from './components/Team';
import Benefits from './components/Benefits';
import CTA from './components/CTA';
import styles from './page.module.css';

export default function Home() {
  return (
    <main className={styles.main}>
      <Hero />
      <Features />
      <Team />
      <Benefits />
      <CTA />

      <footer className={styles.footer}>
        <div className="container">
          <div className={styles.footerContent}>
            <div className={styles.footerBrand}>
              <h3 className="gradient-text">Istaris</h3>
              <p>The future of work is here</p>
            </div>

            <div className={styles.footerLinks}>
              <div className={styles.footerSection}>
                <h4>Product</h4>
                <Link href="#features">Features</Link>
                <Link href="#contact">Get Started</Link>
              </div>

              <div className={styles.footerSection}>
                <h4>Company</h4>
                <Link href="#about">About</Link>
                <Link href="#contact">Contact</Link>
              </div>
            </div>
          </div>

          <div className={styles.footerBottom}>
            <p>&copy; 2026 Istaris. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </main>
  );
}
