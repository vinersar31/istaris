import styles from './Benefits.module.css';

const benefitsData = [
    {
        title: "Instant Deployment",
        text: "Deploy fully trained AI employees in minutes, not months"
    },
    {
        title: "Zero Management Overhead",
        text: "No HR, no training, no performance reviews. Just results."
    },
    {
        title: "Continuous Improvement",
        text: "AI that learns and improves with every interaction"
    },
    {
        title: "Enterprise Security",
        text: "Bank-level encryption and compliance built-in"
    }
];

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
                            Traditional hiring is broken. It&apos;s slow, expensive, and doesn&apos;t scale.
                            Our AI-powered digital employees revolutionize how work gets done.
                        </p>

                        <div className={styles.benefits}>
                            {benefitsData.map((benefit, index) => (
                                <div key={index} className={styles.benefit}>
                                    <div className={styles.benefitIcon}>✓</div>
                                    <div>
                                        <h3 className={styles.benefitTitle}>{benefit.title}</h3>
                                        <p className={styles.benefitText}>{benefit.text}</p>
                                    </div>
                                </div>
                            ))}
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
