import AnimeCard from "@/components/AnimeCard";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
      <h1 className="text-4xl font-bold text-cyan-400 mb-8">My Favorite Anime Cards</h1>

      <div className="flex flex-wrap gap-6 justify-center">
        <AnimeCard
          title="Attack on Titan"
          imageUrl="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTndTb8NdJ4yXP9U8tmod4uG0-Ju61s5KoDSrMbjBhtC_hGLaqhDUA3iXU6IJ_RwoFfpy7C7M4uTQT8C_KT0TMFG_aCrgKJEwXXViK21Loe"
          description="Humanity’s last stand against the terrifying Titans."
        />
        <AnimeCard
          title="Demon Slayer"
          imageUrl="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQz1XJMO9eS5qWaWRFgz40rEiiEtvulOjjY5Bj_-qN-0MsIOUCj9JnQdQTAcuGtnTgPAW6exmZYUiJKjzfw_xj-SjER8IGUSRJzSCmsYXpp0A"
          description="Tanjiro’s fight to save his sister from her demon curse."
        />
        <AnimeCard
          title="Death Note"
          imageUrl="https://upload.wikimedia.org/wikipedia/en/6/6f/Death_Note_Vol_1.jpg"
          description="A high school student discovers a deadly notebook."
        />
      </div>
    </main>
  );
}
