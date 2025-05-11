from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management
otp_store = {}  # Dictionary to store OTPs
logged_users = []

# Simulated function to send OTP (In real application, use an SMS API)
def send_otp(mobile):
    otp = random.randint(1000, 9999)  # Generate 4-digit OTP
    otp_store[mobile] = otp  # Store OTP
    print(f"OTP for {mobile}: {otp}")  # Simulating OTP send
    return otp

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        print("Form submitted!")
        send_otp(mobile)
        session['mobile'] = mobile  # Store mobile in session
        session['name'] = name  # Store name in session
        return redirect(url_for('verify'))
    return '''
    <html>
    <head>
        <style>
        
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f4f4f4;
            }
            
            .container {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
            }
            input {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                width: 100%;
                padding: 10px;
                background: #007BFF;
                border: none;
                color: white;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background: #0056b3;
            }
        </style>
    </head>
    <body>
    
        <div class="container">
            <h2>Login Page</h2>
            <form method="POST">
                <input type="text" name="name" placeholder="Enter Your Name" required>
                <input type="text" name="mobile" placeholder="Enter Mobile Number" required>
                <button type="submit">Send OTP</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    mobile = session.get('mobile')
    if not mobile:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        entered_otp = request.form['otp']
        if otp_store.get(mobile) == int(entered_otp):
            session['logged_in'] = True  # Mark user as logged in
            return redirect(url_for('home'))
        else:
            return "Invalid OTP. Try again!"
    
    return '''
   <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f4f4f4;
            }
            .container {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
            }
            input {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                width: 100%;
                padding: 10px;
                background: #28a745;
                border: none;
                color: white;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background: #218838;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>OTP Verification</h2>
            <form method="POST">
                <input type="text" name="otp" placeholder="Enter OTP" required>
                <button type="submit">Verify OTP</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/dashboard')
def dashboard():
    user_list_html = ""
    for user in logged_users:
        user_list_html += f"<p><strong>Name:</strong> {user['name']}<br><strong>Mobile:</strong> {user['mobile']}</p><hr>"

    return f'''
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f4f4f4;
            }}
            .container {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                width: 400px;
                text-align: center;
            }}
            p {{
                font-size: 16px;
                color: #333;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #28a745;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            a:hover {{
                background: #218838;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>All Logged In Users</h2>
            {user_list_html}
            <a href="/">Go to Home</a>
        </div>
    </body>
    </html>
    '''

@app.route('/about')
def about():
   
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Us - Survilex</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: cooper Hewit;
    }
    body {
      background-color: #f9f9f9;
      color: #333;
      padding: 20px;
    }
     .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: rgb(0, 0, 0);
            padding: 15px 110px;
        }
        .logo {
            font-size: 24px;
            font-weight: bold;
        }
        .nav-links {
            display: flex;
            list-style: none;
        }
        .nav-links li {
            margin-left: 20px;
        }
        .nav-links li a {
            color: rgb(5, 5, 5);
            text-decoration: none;
            font-size: 18px;
        }
        /* Responsive for Mobile */
        @media (max-width: 600px) {
            .header {
                flex-direction: column;
                text-align: center;
            }
            .nav-links {
                margin-top: 10px;
            }
            .nav-links li {
                margin-left: 0;
                margin-top: 5px;
            }
        }
    .container {
      max-width: 1100px;
      margin: auto;
      padding: 20px;
    }
    .title {
      text-align: center;
      font-size: 36px;
      font-weight: bold;
      color: #1d4ed8;
      margin-bottom: 30px;
    }
    .section {
      margin-bottom: 40px;
    }
    .section h2 {
      font-size: 28px;
      color: #1e293b;
      margin-bottom: 10px;
    }
    .section p {
      font-size: 18px;
      line-height: 1.6;
    }
    .founder {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
    .founder img {
      width: 250px;
      height: 250px;
      border-radius: 20px;
      object-fit: cover;
      box-shadow: 0 5px 20px rgba(0,0,0,0.15);
      margin-bottom: 20px;
    }
    .founder h3 {
      font-size: 24px;
      font-weight: bold;
    }
    .founder p.title {
      font-size: 18px;
      color: #1d4ed8;
      margin: 10px 0;
    }
    .founder p.bio {
      font-size: 16px;
      max-width: 700px;
    }
    @media (min-width: 768px) {
      .founder {
        flex-direction: row;
        text-align: left;
      }
      .founder img {
        margin-right: 30px;
        margin-bottom: 0;
      }
    }
       .footer {
    background: #222;
    color: white;
    padding: 30px 110px;
}

.footer-container {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

.footer-section {
    flex: 1;
    margin: 10px;
    min-width: 200px;
}

.footer-section h2, 
.footer-section h3 {
    color: #f4f4f4;
}

.footer-section ul {
    list-style: none;
    padding: 0;
}

.footer-section ul li {
    margin: 8px 0;
}

.footer-section ul li a {
    color: white;
    text-decoration: none;
    transition: 0.3s;
}

.footer-section ul li a:hover {
    text-decoration: underline;
}

.footer-section img {
    width: 30px;
    margin-right: 10px;
}

.footer-bottom {
    text-align: center;
    margin-top: 20px;
    border-top: 1px solid #444;
    padding-top: 10px;
    font-size: 14px;
}

@media (max-width: 768px) {
    .footer-container {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
}
  </style>
</head>
<body>
<header class="header">
        <div class="logo"><img src="https://i.postimg.cc/Qt3ps7n6/Whats-App-Image-2025-05-08-at-08-10-30.jpg"height="100px"width="100px"></div>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            
            <li><a href="login">Login</a></li>
            <li><a href="about">About Us</a></li>
        </ul>
    </header>
  <div class="container">
    <h1 class="title">About Survilex</h1>

    <div class="section">
      <p>
        Survilex is an AI-powered security and smart monitoring company that aims to transform the way we protect our spaces. From homes to businesses, Survilex offers real-time face recognition, unknown person alerts, staff monitoring, motion detection, and entry/exit tracking — all powered by cutting-edge technology.
      </p>
      <p style="margin-top: 15px;">
        Our solutions cater to families, PG hostels, shops, societies, and corporate offices. Whether you're looking to secure your home or monitor a business operation, Survilex adapts to your needs with precision and reliability.
      </p>
      <p style="margin-top: 15px;">
        With a focus on safety, automation, and ease of use, Survilex delivers a smarter way to stay secure. We combine AI, real-time analytics, and user-friendly dashboards to give you control and peace of mind.
      </p>
    </div>

    <div class="section">
      <h2>Our Mission</h2>
      <p>
        To revolutionize everyday security by making AI-based surveillance accessible to families, businesses, and communities. We believe in protection with intelligence — reducing threats before they happen.
      </p>
    </div>

    <div class="section founder">
      <img src="your-image.jpg" alt="Karan - Founder & CEO">
      <div>
        <h3>Karan</h3>
        <p class="title">Founder & CEO, Survilex</p>
        <p class="bio">
          I'm passionate about blending technology with real-world needs. Survilex is my vision of a safer, smarter world — from homes to businesses. Our AI-powered surveillance system not only detects unknown faces but also monitors staff activity, prevents theft, and builds trust through technology.
        </p>
      </div>
    </div>
  </div>
  <footer class="footer">
    <div class="footer-container">
        <div class="footer-section company-info">
            <h2>Survilex</h2>
            <p>Advanced AI-Powered CCTV Face Recognition System</p>
        </div>
        
        <div class="footer-section quick-links">
            <h3>Quick Links</h3>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>

        <div class="footer-section social-media">
            <h3>Follow Us</h3>
            <a href="#"><img src="https://i.postimg.cc/QCkbTbvK/2021-Facebook-icon-svg-removebg-preview.png" alt="Facebook"height="60px" width="60px"></a>
            <a href="#"><img src="https://i.postimg.cc/3wv2G1vr/Instagram-icon-removebg-preview.png" alt="instagram"height="60px" width="60px"></a>
            <a href="#"><img src="https://i.postimg.cc/j2sfGrkC/images-1-removebg-preview.png" alt="LinkedIn"height="60px" width="60px"></a>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; 2025 Survilex. All Rights Reserved.</p>
    </div>
</footer>
</body>
</html>

    '''



@app.route('/')
def home():
   
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Header</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: cooper Hewit;
        }
        body {
            background-color: #f4f4f4;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: rgb(0, 0, 0);
            padding: 15px 110px;
        }
        .logo {
            font-size: 24px;
            font-weight: bold;
        }
        .nav-links {
            display: flex;
            list-style: none;
        }
        .nav-links li {
            margin-left: 20px;
        }
        .nav-links li a {
            color: rgb(5, 5, 5);
            text-decoration: none;
            font-size: 18px;
        }
        /* Responsive for Mobile */
        @media (max-width: 600px) {
            .header {
                flex-direction: column;
                text-align: center;
            }
            .nav-links {
                margin-top: 10px;
            }
            .nav-links li {
                margin-left: 0;
                margin-top: 5px;
            }
        }
        .bg-container {
            width: 100%;
            height: 75vh;
            background-image: url('https://www.nordencommunication.com/public/uploads/media/best-security-camera-systems60631995c7962.jpg'); /* Change this to your image */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .content {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: white;
            font-size: 24px;
            font-weight: bold;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
        }
        .features-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            max-width: 1200px;
            gap: 20px;
            padding: 20px 110px;
            margin: auto;
        }

        .feature-box {
            background: white;
            flex: 1;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        .feature-box h2 {
            color: #333;
            font-size: 22px;
            margin-bottom: 10px;
        }

        .feature-box p {
            color: #555;
            font-size: 16px;
            line-height: 1.5;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .features-container {
                flex-direction: column;
                align-items: center;
                padding: 20px;
            }

            .feature-box {
                width: 100%;
            }
        }
        .footer {
    background: #222;
    color: white;
    padding: 30px 110px;
}

.footer-container {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

.footer-section {
    flex: 1;
    margin: 10px;
    min-width: 200px;
}

.footer-section h2, 
.footer-section h3 {
    color: #f4f4f4;
}

.footer-section ul {
    list-style: none;
    padding: 0;
}

.footer-section ul li {
    margin: 8px 0;
}

.footer-section ul li a {
    color: white;
    text-decoration: none;
    transition: 0.3s;
}

.footer-section ul li a:hover {
    text-decoration: underline;
}

.footer-section img {
    width: 30px;
    margin-right: 10px;
}

.footer-bottom {
    text-align: center;
    margin-top: 20px;
    border-top: 1px solid #444;
    padding-top: 10px;
    font-size: 14px;
}

@media (max-width: 768px) {
    .footer-container {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
}

    </style>
</head>
<body>
    <header class="header">
        <div class="logo"><img src="https://i.postimg.cc/Qt3ps7n6/Whats-App-Image-2025-05-08-at-08-10-30.jpg"height="100px"width="100px"></div>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            
            <li><a href="login">Login</a></li>
            <li><a href="about">About Us</a></li>
        </ul>
    </header>
    <div class="bg-container">
        <div class="content">
            Welcome to My Website
        </div>
    </div>

    <div class="features-container">
        <div class="feature-box">
            <h2>🎯 Real-time Face Recognition</h2>
            <p>Our AI-powered system instantly recognizes faces from your CCTV feed, helping you track known individuals and detect unknown visitors.</p>
        </div>
        <div class="feature-box">
            <h2>📲 Instant Alerts via WhatsApp</h2>
            <p>Get real-time WhatsApp notifications whenever an unrecognized face is detected. Stay informed no matter where you are.</p>
        </div>
    </div>
    <div class="features-container">
        <div class="feature-box">
            <h2>🎯 Real-time Face Recognition</h2>
            <p>Our AI-powered system instantly recognizes faces from your CCTV feed, helping you track known individuals and detect unknown visitors.</p>
        </div>
        <div class="feature-box">
            <h2>📲 Instant Alerts via WhatsApp</h2>
            <p>Get real-time WhatsApp notifications whenever an unrecognized face is detected. Stay informed no matter where you are.</p>
        </div>
    </div>


    <footer class="footer">
    <div class="footer-container">
        <div class="footer-section company-info">
            <h2>Survilex</h2>
            <p>Advanced AI-Powered CCTV Face Recognition System</p>
        </div>
        
        <div class="footer-section quick-links">
            <h3>Quick Links</h3>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>

        <div class="footer-section social-media">
            <h3>Follow Us</h3>
            <a href="#"><img src="https://i.postimg.cc/QCkbTbvK/2021-Facebook-icon-svg-removebg-preview.png" alt="Facebook"height="60px" width="60px"></a>
            <a href="#"><img src="https://i.postimg.cc/3wv2G1vr/Instagram-icon-removebg-preview.png" alt="instagram"height="60px" width="60px"></a>
            <a href="#"><img src="https://i.postimg.cc/j2sfGrkC/images-1-removebg-preview.png" alt="LinkedIn"height="60px" width="60px"></a>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; 2025 Survilex. All Rights Reserved.</p>
    </div>
</footer>

    
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
