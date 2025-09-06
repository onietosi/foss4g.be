export interface Sponsor {
  name: string
  link: string
  logo: string
  bgClass: string
}

export interface SponsorsData {
  gold: Sponsor[]
  silver: Sponsor[]
  bronze: Sponsor[]
}