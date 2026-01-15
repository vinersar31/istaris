'use client';

import styles from './CTA.module.css';

export default function CTA() {
    return (
        <section id="contact" className={`section ${styles.cta}`}>
            <div className="container">
                <div className={styles.content}>
                    <h2 className={styles.title}>
                        Ready to <span className="gradient-text">Transform</span> Your Business?
                    </h2>
                    <p className={styles.subtitle}>
                        Join the future of work. Get started with Istaris AI employees today.
                    </p>

                    <div className={styles.form}>
                        <input
                            type="email"
                            placeholder="Enter your work email"
                            className={styles.input}
                        />
                        <button className="btn btn-primary">
                            Request Demo
                        </button>
                    </div>

                    <p className={styles.disclaimer}>
                        ⚡ Free consultation • No credit card required • Deploy in 24 hours
                    </p>
                </div>
            </div>

            <div className={styles.bgEffect}></div>
        </section>
    );
}
