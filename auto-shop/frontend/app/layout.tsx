import "./globals.css";
import type { Metadata } from "next";
export const metadata: Metadata = { title: "Auto Shop — Find your next car smarter", description: "Australian used-car discovery and market intelligence." };
export default function RootLayout({children}:{children:React.ReactNode}) { return <html lang="en-AU"><body>{children}</body></html>; }
