/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    unoptimized: true, // Takay image loading mein koi issue na ho
  },
};

export default nextConfig;
