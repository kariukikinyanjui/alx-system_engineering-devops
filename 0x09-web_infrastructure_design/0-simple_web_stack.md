# Design of One-Server Web Infrastructure for [www.foobar.com](http://www.foobar.com/):
## User Accesses the Website:
* A user wants to access [www.foobar.com](http://www.foobar.com/) in their web browser.

## Domain Name:
* The user's request is routed via the domain name [www.foobar.com](http://www.foobar.com/)
* The domain name system (DNS) is responsible for translating [www.foobar.com](http://www.foobar.com/) into an IP address, which points to the server hosting the website.

## DNS Record:
* The "www" in [www.foobar.com](http://www.foobar.com/) is a subdomain and typically represents the web server of the domain.
* It is an A DNS record that points to the IP address of the server, in this case, 8.8.8.8

## Sever(8.8.8.8):
* A server is a compouter designed to process reqeuests and deliver data to other computers over a newtwork, in this case, the user's computer.
* The server hosts the entire web infrastructure for [www.foobar.com](http://www.foobar.com/).

## Web Server (Nginx):
* The web server(Nginx) receives incoming HTTP requests from users.
* It handles static content, such as HTML, CSS, and images, and forwards dynamic content requests to the appliaction server.

## Application Server:
* The application server is responsible for processing dynamic content requests. It runs the website's code base(PHP, Python, Ruby).
* The web server communicates with the application server to generate and serve dynamic web pages.

## Application Files (Code Base):
* The code base consists of the website's application files. This is where the website's functionality and logic are defined.

## Database (MySQL):
* The database stores and manages structured data used by the website, such as user profiles, content, and other information.
* The application server communicates with the databasae to retrieve or update data.

## Communication with User's Computer:
* when a user requests [www.foobar.com](http://www.foobar.com/), their web browser sends an HYYP request to the server's IP address (8.8.8.8).
* The server processes the request, which might involve static content(handled by the web server) or dynamic content (handled by the applicattion server).
* Data from the database may be retrieved by the application server, and resulting web page is sent back to the user's computer for display in their web browser.

# Issues with this Infrastructure:
## 1. Single Point of Failure(SPOF):
* The entire infrastructure relies on a single server (8.8.8.8). If this server goes down, the website becomes inaccessible. Implementing redundancy and load balancing can migitate this issue.

## 2. Downtime During Maintenance:
* When updates or maintenance are needed, the web server often needs to be restarted. This can result in downtime for the website. Proper scheduling and redundant servers can help minimize downtime.

## 3. Scalability Challenges:
* This infrastucture is limited in its ability to handle high levels of incoming traffic. Scaling can be difficult, as adding more resources to a single server has limits. To address this, you can consider load balancing and horizontal scaling by adding more servers to distribute traffic.

![One server web infrastructure](https://i.imgur.com/GAe3JCa.png)
