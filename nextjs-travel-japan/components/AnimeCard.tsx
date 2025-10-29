interface AnimeCardProps {
  title: string;
  imageUrl: string;
  description: string;
}

export default function AnimeCard({ title, imageUrl, description }: AnimeCardProps) {
  return (
    <div className="bg-gray-800 rounded-2xl shadow-lg p-6 max-w-sm hover:scale-105 transition-transform duration-300">
      <img src={imageUrl} alt={title} className="rounded-xl mb-4" />
      <h2 className="text-2xl font-semibold text-cyan-400 mb-2">{title}</h2>
      <p className="text-gray-300 text-sm">{description}</p>
    </div>
  );
}
