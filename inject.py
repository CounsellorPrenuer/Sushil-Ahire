import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

packages_html = """
<!-- Hardcoded Mentoria Packages Container -->
<div class='w-full'>
    <!-- Primary Mentoria Plans Tabs -->
    <div class='flex flex-wrap justify-center gap-4 mb-12' id='mentoria-tabs'>
        <button onclick='switchTab(0)' class='tab-btn active bg-blue-600 text-white px-6 py-2 rounded-full font-bold shadow-md'>8-9 STUDENTS</button>
        <button onclick='switchTab(1)' class='tab-btn bg-white text-blue-600 border border-blue-200 px-6 py-2 rounded-full font-bold hover:bg-blue-50'>10-12 STUDENTS</button>
        <button onclick='switchTab(2)' class='tab-btn bg-white text-blue-600 border border-blue-200 px-6 py-2 rounded-full font-bold hover:bg-blue-50'>COLLEGE GRADUATES</button>
        <button onclick='switchTab(3)' class='tab-btn bg-white text-blue-600 border border-blue-200 px-6 py-2 rounded-full font-bold hover:bg-blue-50'>WORKING PROFESSIONALS</button>
    </div>
    
    <div id='tab-contents' class='mb-20'>
        <!-- Tabs will be rendered here by JS -->
    </div>
    
    <div class='text-center mt-20 mb-12'>
        <h2 class='text-4xl font-extrabold text-blue-900 tracking-tight'>Want To Customise Your Mentorship Plan?</h2>
        <p class='text-lg text-gray-600 mt-4 max-w-3xl mx-auto'>If you want to subscribe to specific services from Mentoria that resolve your career challenges, you can choose one or more of the following:</p>
    </div>
    
    <div class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto' id='custom-packages'>
        <!-- Custom packages rendered by JS -->
    </div>
</div>
"""

script_injection = """
        const plansData = [
            {
                title: '8-9 STUDENTS',
                standard: { title: 'Discover', price: '5,500', inc: ['Psychometric assessment to measure your interests', '1 career counselling session with Mentoria\\'s expert career coaches', 'Lifetime access to Knowledge Gateway', 'Invites to live webinars by industry experts'], exc: ['Customised reports after each session with education pathways', 'Guidance on studying abroad', 'CV building during internships/graduation'] },
                premium: { title: 'Discover plus+', price: '15,000', inc: ['Psychometric assessments to measure your interests, personality and abilities', '8 career counselling sessions (1 every year) with Mentoria\\'s expert career coaches until graduation', 'Lifetime access to Knowledge Gateway', 'Invites to live webinars by industry experts', 'Customised reports after each session with education pathways', 'Guidance on studying abroad', 'CV building during internships/graduation'], exc: [] }
            },
            {
                title: '10-12 STUDENTS',
                standard: { title: 'Achieve Online', price: '5,999', inc: ['Psychometric assessment to measure your interests, personality and abilities', '1 career counselling session', 'Lifetime access to Knowledge Gateway', 'Pre-recorded webinars by industry experts'], exc: ['Customised reports after each session with education pathways', 'Guidance on studying abroad', 'CV reviews during internships/graduation'] },
                premium: { title: 'Achieve Plus+', price: '10,599', inc: ['Psychometric assessment to measure your interests, personality and abilities', '4 career counselling sessions', 'Lifetime access to Knowledge Gateway', 'Attend live webinars by industry experts', 'Customised reports after each session with education pathways', 'Guidance on studying abroad', 'CV reviews during internships/graduation'], exc: [] }
            },
            {
                title: 'COLLEGE GRADUATES',
                standard: { title: 'Ascend Online', price: '6,499', inc: ['Psychometric assessment to measure your interests, personality and abilities', '1 career counselling session', 'Lifetime access to Knowledge Gateway', 'Pre-recorded webinars by industry experts'], exc: ['Customised reports after each session with information on certificate/online courses', 'Guidance on studying abroad', 'CV reviews for job application'] },
                premium: { title: 'Ascend Plus+', price: '10,599', inc: ['Psychometric assessment to measure your interests, personality and abilities', '3 career counselling sessions', 'Lifetime access to Knowledge Gateway', 'Attend live webinars by industry experts', 'Customised reports after each session with information on certificate/online courses', 'Guidance on studying abroad', 'CV reviews for job application'], exc: [] }
            },
            {
                title: 'WORKING PROFESSIONALS',
                standard: { title: 'Ascend Online', price: '6,499', inc: ['Psychometric assessment to measure your interests, personality and abilities', '1 career counselling session', 'Lifetime access to Knowledge Gateway', 'Pre-recorded webinars by industry experts'], exc: ['Customised reports after each session with information on certificate/online courses', 'Guidance on studying abroad', 'CV reviews for job application'] },
                premium: { title: 'Ascend Plus+', price: '10,599', inc: ['Psychometric assessment to measure your interests, personality and abilities', '3 career counselling sessions', 'Lifetime access to Knowledge Gateway', 'Attend live webinars by industry experts', 'Customised reports after each session with information on certificate/online courses', 'Guidance on studying abroad', 'CV reviews for job application'], exc: [] }
            }
        ];

        const customPackages = [
            { title: 'CV Building', price: '2,000', desc: 'Is your CV making a great first impression on your behalf? Our HR experts will help you build the kind of CV that stands out from the crowd and increases your chances of getting interview calls.' },
            { title: 'LinkedIn Profile Building', price: '2,000', desc: 'Revamp your LinkedIn profile with recommendations from recruitment experts to showcase your career journey and increase your chances of interview calls.' },
            { title: 'LinkedIn Profile + CV Building', price: '3,500', desc: 'Build the kind of profile recruiters would love to spend time on. Get your CV and LinkedIn profile built by our HR/Recruitment experts.' },
            { title: 'Job Application Strategy', price: '4,000', desc: 'Build the right pipeline for job interviews through a customised job application tracker with information on companies, job postings and steps you need to follow to land your dream job.' },
            { title: 'Career Report', price: '2,500', desc: 'Get a detailed report of your psychometric assessment for a scientific analysis of your interests, personality and abilities. Find out where your interests lie and which future paths you can potentially consider.' },
            { title: 'Career Report + Career Counselling', price: '4,000', desc: 'Connect with India\\'s top career coaches to analyse your psychometric report, get a detailed action plan for your development areas and shortlist the top three career paths you\\'re most likely to enjoy and excel at.' },
            { title: 'Knowledge Gateway + Career Helpline Access', price: '250/month', desc: 'Unlock holistic information on your career paths and get direct access to Mentoria\\'s experts, who will resolve your career-related queries through our dedicated Career Helpline. Validate your career decisions from now until you land a job you love.' },
            { title: 'One-to-One Session with a Career Expert', price: '3,500 per interaction for 1 hour', desc: 'Resolve your career queries and glimpse into your future world through a one-on-one session with an expert from your chosen field.' },
            { title: 'Overseas Admission Planner', price: '3,000 for a planner with top 10 colleges in India OR any 1 country abroad', desc: 'Planning your masters studies? Get unbiased recommendations and details on your future college options in India and abroad, organised in one resourceful planner.' },
            { title: 'Overseas Admission: SOP Brainstorm', price: '3,000 for a one-hour session', desc: 'Increase your chances of getting admissions in your dream college by structuring your SOP in the most ideal manner through discussions with an overseas admissions expert.' },
            { title: 'Overseas Admission: SOP Review', price: '2,500', desc: 'Is your SOP/Essay good enough to get you shortlisted? Get it reviewed by our team of overseas admissions experts to make sure you make the cut.' },
            { title: 'Interview Prep Session', price: '2,000', desc: 'Ace your upcoming interviews with guidance from India\\'s top HR experts and increase your chances of landing your dream job.' }
        ];

        function renderTab(index) {
            const data = plansData[index];
            
            function buildList(inc, exc) {
                let htmlStr = '';
                inc.forEach(i => {
                    htmlStr += `<li class="flex items-start gap-3 text-sm text-gray-700"><svg class="w-5 h-5 text-blue-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg><span>${i}</span></li>`;
                });
                exc.forEach(e => {
                    htmlStr += `<li class="flex items-start gap-3 text-sm text-gray-400"><svg class="w-5 h-5 text-blue-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg><span>${e}</span></li>`;
                });
                return htmlStr;
            }

            document.getElementById('tab-contents').innerHTML = `
                <div class="relative max-w-5xl mx-auto flex flex-col md:flex-row gap-8 justify-center">
                    <div class="absolute -left-12 top-1/4 w-64 h-64 bg-yellow-400 rounded-full mix-blend-multiply filter blur-sm opacity-70 hidden md:block"></div>
                    <div class="absolute -right-8 -top-8 w-32 h-32 bg-pink-600 rounded-full mix-blend-multiply filter blur-sm opacity-70 hidden md:block"></div>

                    <div class="bg-white rounded-3xl p-8 shadow-xl border border-gray-100 flex flex-col w-full md:w-1/2 z-10">
                        <div class="text-blue-400 text-sm font-bold mb-4">STANDARD</div>
                        <div class="text-center mb-8">
                            <h3 class="text-3xl font-bold text-blue-500 mb-2">${data.standard.title}</h3>
                            <div class="text-4xl font-extrabold text-blue-500">? ${data.standard.price}</div>
                        </div>
                        <ul class="space-y-4 mb-8 flex-1">${buildList(data.standard.inc, data.standard.exc)}</ul>
                        <button onclick="window.location.href='#contact'" class="w-full bg-[#5865F2] text-white py-3 rounded-full font-bold hover:bg-blue-600 transition shadow-md">BUY NOW</button>
                    </div>

                    <div class="bg-white rounded-3xl p-8 shadow-xl border border-gray-100 flex flex-col w-full md:w-1/2 z-10">
                        <div class="text-blue-400 text-sm font-bold mb-4">PREMIUM</div>
                        <div class="text-center mb-8">
                            <h3 class="text-3xl font-bold text-blue-600 mb-2">${data.premium.title}</h3>
                            <div class="text-4xl font-extrabold text-blue-600">? ${data.premium.price}</div>
                        </div>
                        <ul class="space-y-4 mb-8 flex-1">${buildList(data.premium.inc, data.premium.exc)}</ul>
                        <button onclick="window.location.href='#contact'" class="w-full bg-[#2942d4] text-white py-3 rounded-full font-bold hover:bg-blue-800 transition shadow-md">BUY NOW</button>
                    </div>
                </div>
            `;
        }

        window.switchTab = function(index) {
            document.querySelectorAll('.tab-btn').forEach((btn, i) => {
                if (i === index) {
                    btn.className = 'tab-btn active bg-blue-600 text-white px-6 py-2 rounded-full font-bold shadow-md';
                } else {
                    btn.className = 'tab-btn bg-white text-blue-600 border border-blue-200 px-6 py-2 rounded-full font-bold hover:bg-blue-50';
                }
            });
            renderTab(index);
        }

        function renderCustomPackages() {
            let htmlStr = '';
            customPackages.forEach(pkg => {
                htmlStr += `
                    <div class="bg-white border border-gray-200 rounded-xl p-6 flex flex-col shadow-sm hover:shadow-md transition">
                        <h4 class="text-xl font-bold text-blue-900 mb-1">${pkg.title}</h4>
                        <div class="text-blue-600 font-bold mb-4">? ${pkg.price}</div>
                        <p class="text-sm text-gray-600 flex-1 mb-6">${pkg.desc}</p>
                        <button onclick="window.location.href='#contact'" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg self-start transition">BUY NOW</button>
                    </div>
                `;
            });
            document.getElementById('custom-packages').innerHTML = htmlStr;
        }
"""

container_regex = re.compile(r'<div id="packages-container" class="w-full">.*?</div>\s*</div>\s*</section>', re.DOTALL)
html = container_regex.sub(f'<div id="packages-container" class="w-full">{packages_html}</div></div></section>', html)

sanity_regex = re.compile(r'// Fetch Mentoria Packages.*?catch \(err\) \{', re.DOTALL)
html = sanity_regex.sub(f'// Mentoria Packages logic replaced with hardcoded data\n{script_injection}\n        renderTab(0);\n        renderCustomPackages();\n        }} catch (err) {{', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
