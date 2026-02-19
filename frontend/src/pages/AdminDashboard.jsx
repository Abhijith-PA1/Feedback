import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

function AdminDashboard() {
    const navigate = useNavigate()
    const [analytics, setAnalytics] = useState({
        totalUsers: 0,
        totalFeedback: 0,
        averageRating: 0,
        sentimentSummary: { positive: 0, negative: 0, neutral: 0 },
    })
    const [feedbacks, setFeedbacks] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        fetchDashboard()
    }, [])

    const fetchDashboard = async () => {
        try {
            const token = localStorage.getItem('token')
            const res = await axios.get('/api/admin/dashboard', {
                headers: { Authorization: `Bearer ${token}` },
            })
            setAnalytics(res.data.analytics)
            setFeedbacks(res.data.feedbacks)
        } catch (err) {
            if (err.response?.status === 401 || err.response?.status === 403) {
                localStorage.removeItem('token')
                localStorage.removeItem('role')
                localStorage.removeItem('userName')
                navigate('/login')
            }
        } finally {
            setLoading(false)
        }
    }

    const handleLogout = () => {
        localStorage.removeItem('token')
        localStorage.removeItem('role')
        localStorage.removeItem('userName')
        navigate('/login')
    }

    const getSentimentBadge = (sentiment) => {
        const styles = {
            positive: 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30',
            negative: 'bg-red-500/20 text-red-400 border-red-500/30',
            neutral: 'bg-slate-500/20 text-slate-400 border-slate-500/30',
        }
        return styles[sentiment] || styles.neutral
    }

    const summaryCards = [
        {
            title: 'Total Users',
            value: analytics.totalUsers,
            icon: (
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
            ),
            gradient: 'from-violet-500 to-purple-600',
            shadow: 'shadow-purple-500/20',
        },
        {
            title: 'Total Feedback',
            value: analytics.totalFeedback,
            icon: (
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                </svg>
            ),
            gradient: 'from-cyan-500 to-blue-600',
            shadow: 'shadow-blue-500/20',
        },
        {
            title: 'Average Rating',
            value: analytics.averageRating?.toFixed(1) || '0.0',
            icon: (
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                </svg>
            ),
            gradient: 'from-amber-500 to-orange-600',
            shadow: 'shadow-orange-500/20',
        },
        {
            title: 'Sentiment',
            value: `👍${analytics.sentimentSummary?.positive || 0}  👎${analytics.sentimentSummary?.negative || 0}  😐${analytics.sentimentSummary?.neutral || 0}`,
            icon: (
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
            ),
            gradient: 'from-emerald-500 to-teal-600',
            shadow: 'shadow-teal-500/20',
            smallText: true,
        },
    ]

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center">
                <div className="flex flex-col items-center gap-4">
                    <svg className="animate-spin h-10 w-10 text-purple-400" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                    </svg>
                    <p className="text-slate-400">Loading dashboard...</p>
                </div>
            </div>
        )
    }

    return (
        <div className="min-h-screen p-4 md:p-6">
            {/* Navbar */}
            <nav className="max-w-7xl mx-auto flex items-center justify-between mb-8 py-4">
                <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 flex items-center justify-center shadow-lg shadow-purple-500/20">
                        <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                        </svg>
                    </div>
                    <span className="text-white font-semibold text-lg">Admin Dashboard</span>
                </div>
                <button
                    onClick={handleLogout}
                    className="px-4 py-2 rounded-lg bg-white/10 hover:bg-white/20 text-slate-300 hover:text-white text-sm font-medium border border-white/10 transition-all duration-200 cursor-pointer"
                >
                    Logout
                </button>
            </nav>

            <div className="max-w-7xl mx-auto">
                {/* Summary Cards */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
                    {summaryCards.map((card) => (
                        <div
                            key={card.title}
                            className="bg-white/10 backdrop-blur-xl border border-white/20 rounded-2xl p-6 hover:bg-white/15 transition-all duration-300"
                        >
                            <div className="flex items-center justify-between mb-4">
                                <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${card.gradient} flex items-center justify-center shadow-lg ${card.shadow} text-white`}>
                                    {card.icon}
                                </div>
                            </div>
                            <p className="text-slate-400 text-sm">{card.title}</p>
                            <p className={`font-bold mt-1 ${card.smallText ? 'text-lg text-white' : 'text-3xl text-white'}`}>
                                {card.value}
                            </p>
                        </div>
                    ))}
                </div>

                {/* Feedback Table */}
                <div className="bg-white/10 backdrop-blur-xl border border-white/20 rounded-2xl overflow-hidden">
                    <div className="p-6 border-b border-white/10">
                        <h2 className="text-xl font-bold text-white">All Feedback</h2>
                        <p className="text-slate-400 text-sm mt-1">Review user feedback with AI sentiment analysis</p>
                    </div>

                    <div className="overflow-x-auto">
                        <table className="w-full">
                            <thead>
                                <tr className="border-b border-white/10">
                                    <th className="px-6 py-4 text-left text-xs font-semibold text-slate-400 uppercase tracking-wider">User</th>
                                    <th className="px-6 py-4 text-left text-xs font-semibold text-slate-400 uppercase tracking-wider">Rating</th>
                                    <th className="px-6 py-4 text-left text-xs font-semibold text-slate-400 uppercase tracking-wider">Comment</th>
                                    <th className="px-6 py-4 text-left text-xs font-semibold text-slate-400 uppercase tracking-wider">Sentiment</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-white/5">
                                {feedbacks.length === 0 ? (
                                    <tr>
                                        <td colSpan={4} className="px-6 py-12 text-center text-slate-400">
                                            No feedback submitted yet
                                        </td>
                                    </tr>
                                ) : (
                                    feedbacks.map((fb, idx) => (
                                        <tr key={idx} className="hover:bg-white/5 transition-colors duration-150">
                                            <td className="px-6 py-4">
                                                <div className="flex items-center gap-3">
                                                    <div className="w-8 h-8 rounded-full bg-gradient-to-br from-violet-500 to-purple-600 flex items-center justify-center text-white text-sm font-medium">
                                                        {fb.userName?.charAt(0)?.toUpperCase() || 'U'}
                                                    </div>
                                                    <span className="text-white text-sm font-medium">{fb.userName || 'Unknown'}</span>
                                                </div>
                                            </td>
                                            <td className="px-6 py-4">
                                                <div className="flex items-center gap-1">
                                                    {[...Array(5)].map((_, i) => (
                                                        <span key={i} className={`text-sm ${i < fb.rating ? 'text-amber-400' : 'text-slate-600'}`}>★</span>
                                                    ))}
                                                </div>
                                            </td>
                                            <td className="px-6 py-4 text-slate-300 text-sm max-w-xs truncate">{fb.comment}</td>
                                            <td className="px-6 py-4">
                                                <span className={`inline-flex px-3 py-1 rounded-full text-xs font-medium border ${getSentimentBadge(fb.sentiment)}`}>
                                                    {fb.sentiment || 'N/A'}
                                                </span>
                                            </td>
                                        </tr>
                                    ))
                                )}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default AdminDashboard
