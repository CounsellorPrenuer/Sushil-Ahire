import { client } from '../sanity/lib/client';

export const revalidate = 60; // Revalidate every 60 seconds

export default async function Home() {
  const founderInfo = await client.fetch(`*[_type == "founder"][0]`);
  const mentoriaPackages = await client.fetch(`*[_type == "mentoriaPackage"] | order(order asc)`);

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 font-sans">
      <nav className="flex justify-between items-center p-6 bg-white shadow-md sticky top-0 z-50">
        <div className="font-bold text-2xl tracking-tighter">Future Map</div>
        <div className="hidden md:flex gap-6">
          <a href="#home" className="hover:text-blue-600 transition">Home</a>
          <a href="#founder" className="hover:text-blue-600 transition">About Founder</a>
          <a href="#services" className="hover:text-blue-600 transition">Services</a>
          <a href="#packages" className="hover:text-blue-600 transition">Mentoria Packages</a>
          <a href="#testimonials" className="hover:text-blue-600 transition">Testimonials</a>
          <a href="#contact" className="hover:text-blue-600 transition">Contact Us</a>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto p-6 md:p-12 space-y-24">
        {/* Hero Section */}
        <section id="home" className="text-center py-20">
          <h1 className="text-5xl md:text-7xl font-extrabold text-blue-900 mb-6 tracking-tight">
            From Classroom to Boardroom
          </h1>
          <p className="text-xl md:text-2xl text-gray-600 max-w-3xl mx-auto mb-10">
            A job is what you do, a career is the story of how you contributed. My role is to make sure that story is a bestseller.
          </p>
          <a href="#contact" className="bg-blue-600 text-white px-8 py-4 rounded-full font-bold hover:bg-blue-700 transition">
            Book a Consultation
          </a>
        </section>

        {/* Founder Section */}
        <section id="founder" className="grid md:grid-cols-2 gap-12 items-center bg-white p-8 rounded-2xl shadow-sm">
          <div>
            <h2 className="text-3xl font-bold mb-4">Meet {founderInfo?.name || 'Dr Sushil Ahire'}</h2>
            <h3 className="text-xl text-blue-600 mb-6">{founderInfo?.title || 'Strategic Analyst & Career Counselor'}</h3>
            <p className="text-gray-700 text-lg leading-relaxed mb-6">
              {founderInfo?.philosophy || 'Mission: Translate client\'s unique value into market dominance. We help students, professionals, and corporates find their perfect career path.'}
            </p>
          </div>
          <div className="h-96 bg-gray-200 rounded-xl flex items-center justify-center overflow-hidden">
             {/* We will load the sanity image here */}
             <div className="text-gray-400">Founder Image</div>
          </div>
        </section>

        {/* Packages Section */}
        <section id="packages">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold mb-4">Mentoria Packages</h2>
            <p className="text-gray-600 text-lg">Premium guidance tailored for your specific career stage.</p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {mentoriaPackages?.length > 0 ? (
              mentoriaPackages.map((pkg: any) => (
                <div key={pkg._id} className="bg-white rounded-2xl shadow-lg overflow-hidden flex flex-col">
                  <div className="h-48 bg-gray-200 w-full"></div>
                  <div className="p-6 flex-1 flex flex-col">
                    <h3 className="text-2xl font-bold mb-2">{pkg.title}</h3>
                    <p className="text-gray-600 mb-4 flex-1">{pkg.description}</p>
                    <div className="text-xl font-bold text-blue-600 mb-4">{pkg.price}</div>
                    <button className="w-full bg-gray-900 text-white py-3 rounded-lg font-medium hover:bg-gray-800 transition">
                      Learn More
                    </button>
                  </div>
                </div>
              ))
            ) : (
              <div className="col-span-full text-center text-gray-500 py-12 bg-gray-50 rounded-2xl border-2 border-dashed">
                Packages will appear here once added in Sanity Studio.
              </div>
            )}
          </div>
        </section>
      </main>

      <footer className="bg-gray-900 text-white py-12 text-center mt-24">
        <p>© 2026 Future Map. All rights reserved.</p>
      </footer>
    </div>
  );
}
