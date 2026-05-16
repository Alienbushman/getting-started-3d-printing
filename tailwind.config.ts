import type { Config } from 'tailwindcss';

export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    colors: {
      bg: '#FAF8F4',
      ink: '#1A1A1A',
      accent: '#E85D2F',
      'accent-soft': '#FCE4D6',
      success: '#2D8F47',
      warning: '#D97706',
      danger: '#C53030',
      'neutral-50': '#F4F2EE',
      'neutral-100': '#E5E2DC',
      'neutral-300': '#A8A39A',
      'neutral-500': '#6B675F',
      'neutral-900': '#2A2724',
      white: '#ffffff',
      transparent: 'transparent',
    },
    fontFamily: {
      display: ['"Space Grotesk"', 'system-ui', 'sans-serif'],
      sans: ['Inter', 'system-ui', 'sans-serif'],
    },
    fontSize: {
      xs: ['12px', { lineHeight: '1.4' }],
      sm: ['14px', { lineHeight: '1.5' }],
      base: ['16px', { lineHeight: '1.6' }],
      lg: ['18px', { lineHeight: '1.5' }],
      xl: ['22px', { lineHeight: '1.4' }],
      '2xl': ['28px', { lineHeight: '1.3' }],
      '3xl': ['36px', { lineHeight: '1.2' }],
    },
    borderRadius: {
      none: '0',
      sm: '2px',
      DEFAULT: '4px',
      lg: '8px',
      '2xl': '16px',
    },
    extend: {
      maxWidth: {
        content: '1100px',
      },
    },
  },
  plugins: [],
} satisfies Config;
