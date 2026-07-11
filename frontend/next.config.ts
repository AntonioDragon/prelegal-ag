import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Static export so the frontend can be served by FastAPI in production.
  output: "export",
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
