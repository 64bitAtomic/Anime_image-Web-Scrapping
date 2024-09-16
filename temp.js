const anime = [
  {
    anime_id: 32281,
    name: "Kimi no Na wa.",
    genre: "Drama, Romance, School, Supernatural",
    type: "Movie",
    episodes: 1,
    rating: 9.37,
    members: 200630,
    image_url: "https://cdn.myanimelist.net/images/anime/5/87048.jpg",
  },
  {
    anime_id: 5114,
    name: "Fullmetal Alchemist: Brotherhood",
    genre: "Action, Adventure, Drama, Fantasy, Magic, Military, Shounen",
    type: "TV",
    episodes: 64,
    rating: 9.26,
    members: 793665,
    image_url: "https://cdn.myanimelist.net/images/anime/1223/96541.jpg",
  },
  {
    anime_id: 28977,
    name: "Gintama°",
    genre: "Action, Comedy, Historical, Parody, Samurai, Sci-Fi, Shounen",
    type: "TV",
    episodes: 51,
    rating: 9.25,
    members: 114262,
    image_url: "https://cdn.myanimelist.net/images/anime/3/72078.jpg",
  },
];

anime.map((item) => {
  if (item.genre.includes("Romance")) {
    console.log(item.name);
  }
});
