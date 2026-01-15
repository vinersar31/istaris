import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Istaris - Stop Hiring Humans",
  description: "AI-powered automation that replaces traditional roles. Scale your business without increasing headcount.",
  keywords: "AI automation, digital employees, AI BDR, scrum master AI, digital marketing AI",
  authors: [{ name: "Istaris" }],
  openGraph: {
    title: "Istaris - Stop Hiring Humans",
    description: "AI-powered automation that replaces traditional roles",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
