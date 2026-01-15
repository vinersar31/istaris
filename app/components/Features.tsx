'use client';

import styles from './Features.module.css';

const features = [
    {
        icon: '🤖',
        title: 'AI-Powered Automation',
        description: 'Advanced AI models that understand context, make decisions, and execute tasks with human-level intelligence.'
    },
    {
        icon: '⚡',
        title: 'Lightning Fast',
        description: 'Process thousands of tasks simultaneously. What takes humans days, our AI completes in minutes.'
    },
    {
        icon: '🌍',
        title: '24/7 Global Operations',
        description: 'Never sleep, never take breaks. Your digital employees work around the clock, across all time zones.'
    },
    {
        icon: '📈',
        title: 'Infinite Scalability',
        description: 'Scale instantly without hiring, training, or managing. Add capacity with a single click.'
    },
    {
        icon: '💰',
        title: 'Cost Efficient',
        description: 'Reduce operational costs by up to 90%. No salaries, benefits, or overhead expenses.'
    },
    {
        icon: '🎯',
        title: 'Perfect Accuracy',
        description: 'Eliminate human error. Consistent, precise results every single time, guaranteed.'
    }
];

export default function Features() {
    return (
        <section id="features" className={`section ${styles.features}`}>
            <div className="container">
                <div className={styles.header}>
                    <h2 className={styles.title}>
                        The Future of <span className="gradient-text">Work</span>
                    </h2>
                    <p className={styles.subtitle}>
                        Digital employees that outperform traditional teams in every metric
                    </p>
                </div>

                <div className={styles.grid}>
                    {features.map((feature, index) => (
                        <div
                            key={index}
                            className={`card ${styles.card}`}
                            style={{ animationDelay: `${index * 100}ms` }}
                        >
                            <div className={styles.icon}>{feature.icon}</div>
                            <h3 className={styles.cardTitle}>{feature.title}</h3>
                            <p className={styles.cardDescription}>{feature.description}</p>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}
