
import styles from './Team.module.css';

const basePath = process.env.NODE_ENV === 'production' ? '/istaris' : '';

const teamMembers = [
    {
        name: 'Marcus',
        role: 'AI Scrum Master',
        image: '/images/marcus-scrum-master.png',
        description: 'Meet Marcus, your dedicated AI Scrum Master. He orchestrates perfect sprints, manages your backlog, and ensures your team stays on track 24/7. Never misses a standup, never takes a vacation.',
        skills: ['Sprint Planning', 'Backlog Management', 'Team Coordination', 'Agile Coaching']
    },
    {
        name: 'Sophia',
        role: 'AI Digital Marketing Specialist',
        image: '/images/sophia-marketing.png',
        description: 'Meet Sophia, your AI-powered Digital Marketing Specialist. She crafts compelling campaigns, analyzes performance in real-time, and optimizes your marketing ROI while you sleep.',
        skills: ['Campaign Management', 'SEO Optimization', 'Content Strategy', 'Analytics & Reporting']
    }
];

export default function Team() {
    return (
        <section className={`section ${styles.team}`}>
            <div className="container">
                <div className={styles.header}>
                    <h2 className={styles.title}>
                        Meet Your <span className="gradient-text">Digital Employees</span>
                    </h2>
                    <p className={styles.subtitle}>
                        Real expertise. Zero overhead. Available 24/7.
                    </p>
                </div>

                <div className={styles.grid}>
                    {teamMembers.map((member, index) => (
                        <div
                            key={index}
                            className={`${styles.card} glass`}
                            style={{ animationDelay: `${index * 200}ms` }}
                        >
                            <div className={styles.imageWrapper}>
                                <img
                                    src={`${basePath}${member.image}`}
                                    alt={`${member.name} - ${member.role}`}
                                    className={styles.image}
                                />
                                <div className={styles.badge}>
                                    <span className={styles.dot}></span>
                                    Active Now
                                </div>
                            </div>

                            <div className={styles.content}>
                                <h3 className={styles.name}>{member.name}</h3>
                                <p className={styles.role}>{member.role}</p>
                                <p className={styles.description}>{member.description}</p>

                                <div className={styles.skills}>
                                    {member.skills.map((skill, i) => (
                                        <span key={i} className={styles.skill}>
                                            {skill}
                                        </span>
                                    ))}
                                </div>

                                <button className={`btn btn-primary ${styles.hireBtn}`}>
                                    Hire {member.name}
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}
