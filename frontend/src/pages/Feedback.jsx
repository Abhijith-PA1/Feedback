import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

function Feedback() {
    const navigate = useNavigate()
    const userName = localStorage.getItem('userName') || 'User'
    const [rating, setRating] = useState('')
    const [comment, setComment] = useState('')
    const [error, setError] = useState('')
    const [success, setSuccess] = useState('')
    const [loading, setLoading] = useState(false)

    const handleLogout = () => {
        localStorage.removeItem('token')
        localStorage.removeItem('role')
        localStorage.removeItem('userName')
        navigate('/login')
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        setError('')
        setSuccess('')

        if (!rating || !comment.trim()) {
            setError('Please provide both a rating and a comment')
            return
        }

        setLoading(true)
        try {
            const token = localStorage.getItem('token')
            const res = await axios.post(
                '/api/feedback',
                { rating: parseInt(rating), comment },
                { headers: { Authorization: `Bearer ${token}` } }
            )
            setSuccess(res.data.message || 'Feedback submitted successfully!')
            setRating('')
            setComment('')
        } catch (err) {
            if (err.response?.status === 401) {
                localStorage.removeItem('token')
                localStorage.removeItem('role')
                localStorage.removeItem('userName')
                navigate('/login')
                return
            }
            setError(err.response?.data?.error || 'Failed to submit feedback')
        } finally {
            setLoading(false)
        }
    }

    const stars = [1, 2, 3, 4, 5]

    return (
        <div className="min-h-screen p-4">
            {/* Navbar */}
            <nav className="max-w-4xl mx-auto flex items-center justify-between mb-8 py-4">
                <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center shadow-lg shadow-emerald-500/20">
                        <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                        </svg>
                    </div>
                    <span className="text-white font-semibold text-lg">Feedback Portal</span>
                </div>
                <div className="flex items-center gap-4">
                    <span className="text-slate-300 text-sm hidden sm:block">Hi, {userName}</span>
                    <button
                        onClick={handleLogout}
                        className="px-4 py-2 rounded-lg bg-white/10 hover:bg-white/20 text-slate-300 hover:text-white text-sm font-medium border border-white/10 transition-all duration-200 cursor-pointer"
                    >
                        Logout
                    </button>
                </div>
            </nav>

            {/* Feedback Card */}
            <div className="max-w-2xl mx-auto">
                <div className="text-center mb-8">
                    <h1 className="text-3xl font-bold text-white">Share Your Feedback</h1>
                    <p className="text-slate-400 mt-2">We value your opinion. Help us improve!</p>
                </div>

                <div className="bg-white/10 backdrop-blur-xl border border-white/20 rounded-2xl shadow-2xl p-8">
                    {error && (
                        <div className="mb-4 p-3 rounded-lg bg-red-500/20 border border-red-500/30 text-red-300 text-sm flex items-center gap-2">
                            <svg className="w-4 h-4 shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                            </svg>
                            {error}
                        </div>
                    )}
                    {success && (
                        <div className="mb-4 p-3 rounded-lg bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 text-sm flex items-center gap-2">
                            <svg className="w-4 h-4 shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                            </svg>
                            {success}
                        </div>
                    )}

                    <form onSubmit={handleSubmit} className="space-y-6">
                        {/* Star Rating */}
                        <div>
                            <label className="block text-sm font-medium text-slate-300 mb-3">Rating</label>
                            <div className="flex gap-2">
                                {stars.map((star) => (
                                    <button
                                        key={star}
                                        type="button"
                                        onClick={() => setRating(star.toString())}
                                        className={`w-12 h-12 rounded-xl flex items-center justify-center text-xl transition-all duration-200 cursor-pointer ${parseInt(rating) >= star
                                                ? 'bg-amber-500/30 border-amber-400/50 text-amber-400 shadow-lg shadow-amber-500/20'
                                                : 'bg-white/5 border-white/10 text-slate-500 hover:bg-white/10 hover:text-slate-300'
                                            } border`}
                                    >
                                        ★
                                    </button>
                                ))}
                            </div>
                            {rating && (
                                <p className="mt-2 text-sm text-slate-400">
                                    You selected <span className="text-amber-400 font-medium">{rating}/5</span>
                                </p>
                            )}
                        </div>

                        {/* Comment */}
                        <div>
                            <label className="block text-sm font-medium text-slate-300 mb-1.5">Your Comments</label>
                            <textarea
                                value={comment}
                                onChange={(e) => setComment(e.target.value)}
                                rows={4}
                                className="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-all duration-200 resize-none"
                                placeholder="Tell us about your experience..."
                            />
                        </div>

                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full py-3 px-4 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-semibold shadow-lg shadow-emerald-500/25 hover:shadow-emerald-500/40 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer"
                        >
                            {loading ? (
                                <span className="flex items-center justify-center gap-2">
                                    <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                                    </svg>
                                    Submitting...
                                </span>
                            ) : 'Submit Feedback'}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Feedback
