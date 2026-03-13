'use client';

import Link from 'next/link';
import styles from './Hero.module.css';

export default function Hero() {
    return (
        <section className={styles.hero}>
            <div className="container">
                <div className={styles.content}>
                    <h1 className={`${styles.title} animate-fade-in-up`}>
                        Stop Hiring <span className="gradient-text">Humans</span>
                    </h1>

                    <p className={`${styles.subtitle} animate-fade-in-up`}>
                        AI-powered digital employees that work 24/7 to automate your entire workflow.
                        No breaks. No mistakes. No limits.
                    </p>

                    <div className={`${styles.cta} animate-fade-in-up`}>
                        <Link href="#contact" className="btn btn-primary">
                            Get Started
                        </Link>
                        <Link href="#features" className="btn btn-secondary">
                            Learn More
                        </Link>
                    </div>

                    <div className={styles.stats}>
                        <div className={styles.stat}>
                            <div className={styles.statValue}>99.9%</div>
                            <div className={styles.statLabel}>Uptime</div>
                        </div>
                        <div className={styles.stat}>
                            <div className={styles.statValue}>24/7</div>
                            <div className={styles.statLabel}>Always Working</div>
                        </div>
                        <div className={styles.stat}>
                            <div className={styles.statValue}>10x</div>
                            <div className={styles.statLabel}>Productivity Boost</div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Background Effects */}
            <div className={styles.bgGradient}></div>
            <div className={styles.bgGrid}></div>
        </section>
    );
}
