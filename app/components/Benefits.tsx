'use client';

import styles from './Benefits.module.css';

export default function Benefits() {
    return (
        <section className={`section ${styles.benefits}`}>
            <div className="container">
                <div className={styles.content}>
                    <div className={styles.textContent}>
                        <h2 className={styles.title}>
                            Why Choose <span className="gradient-text">Istaris</span>?
                        </h2>
                        <p className={styles.description}>
                            Traditional hiring is broken. It's slow, expensive, and doesn't scale.
                            Our AI-powered digital employees revolutionize how work gets done.
                        </p>

                        <div className={styles.benefits}>
                            <div className={styles.benefit}>
                                <div className={styles.benefitIcon}>✓</div>
                                <div>
                                    <h3 className={styles.benefitTitle}>Instant Deployment</h3>
                                    <p className={styles.benefitText}>
                                        Deploy fully trained AI employees in minutes, not months
                                    </p>
                                </div>
                            </div>

                            <div className={styles.benefit}>
                                <div className={styles.benefitIcon}>✓</div>
                                <div>
                                    <h3 className={styles.benefitTitle}>Zero Management Overhead</h3>
                                    <p className={styles.benefitText}>
                                        No HR, no training, no performance reviews. Just results.
                                    </p>
                                </div>
                            </div>

                            <div className={styles.benefit}>
                                <div className={styles.benefitIcon}>✓</div>
                                <div>
                                    <h3 className={styles.benefitTitle}>Continuous Improvement</h3>
                                    <p className={styles.benefitText}>
                                        AI that learns and improves with every interaction
                                    </p>
                                </div>
                            </div>

                            <div className={styles.benefit}>
                                <div className={styles.benefitIcon}>✓</div>
                                <div>
                                    <h3 className={styles.benefitTitle}>Enterprise Security</h3>
                                    <p className={styles.benefitText}>
                                        Bank-level encryption and compliance built-in
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className={styles.visual}>
                        <div className={`${styles.statsCard} glass`}>
                            <div className={styles.statsRow}>
                                <div className={styles.statsItem}>
                                    <div className={styles.statsNumber}>90%</div>
                                    <div className={styles.statsLabel}>Cost Reduction</div>
                                </div>
                                <div className={styles.statsItem}>
                                    <div className={styles.statsNumber}>5x</div>
                                    <div className={styles.statsLabel}>Faster Output</div>
                                </div>
                            </div>
                            <div className={styles.statsRow}>
                                <div className={styles.statsItem}>
                                    <div className={styles.statsNumber}>100%</div>
                                    <div className={styles.statsLabel}>Accuracy Rate</div>
                                </div>
                                <div className={styles.statsItem}>
                                    <div className={styles.statsNumber}>∞</div>
                                    <div className={styles.statsLabel}>Scalability</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
