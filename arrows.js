<div className="absolute left-2/2 top-[50px] -ml-3 w-6 h-6 animate-bounce">
            <span className="block w-6 h-6 border-l border-b border-white transform rotate-[-360deg]"></span>
            <span className="block w-6 h-6 border-l border-b border-white transform rotate-[-90deg]"></span>
            <span className="block w-6 h-6 border-l border-b border-white transform rotate-[-45deg]"></span>
          </div>

          {/* Animated Arrow Moving Left and Right */}
          <div className="absolute left-2/2 top-[300px] -ml-3 w-6 h-6" style={{
            animation: 'wiggle 1.5s infinite ease-in-out'
          }}>
            <style>
              {`
                @keyframes wiggle {
                  0%, 100% { transform: translateX(0) rotate(-45deg); }
                  50% { transform: translateX(20px) rotate(-45deg); }
                }
              `}
            </style>
            <span className="block w-6 h-6 border-l border-b border-white transform rotate-[-45deg]"></span>
          </div>
