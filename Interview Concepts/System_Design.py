# This contains all low level and high level designing concepts

'''SYSTEM DESIGN FOUNDATIONS + HLD THINKING(1/10)'''
# System Design is the process of deciding how software components, data, communication, and infrastructure works together to satisfy functional and non-functional requirements under realistic constraints.
# There are many constraints in it. And due to these there is rarely a single "correct Architecture". So, we will be choosing between the trade-offs

'''HLD vs LLD'''
# HLD answers what major components does the system have, and how do they communicate?
# It mainly focuses on big things like servers, load balencers, app servers, database, cache, queues, communication, scalability, availability, failures
# LLD goes inside a component and designs in that.
# Ex: Parking lot designing:
# HLD: says User->Load Balancer->API Gateway->Micro Services(Auth Service,Payment Service,Order Service)->Redis Cache->Database->Kafka Queue
# LLD: says parkinglot has floor, parkingSpot, vechile, ticket, payment. And then it goes inside the vechile and again designs the vechile as the car, bike, etc
# In LLD we will be thinking about the classes, interfaces, objects, methods, relationships, SOLID, extensibility, design patterns

# | HLD | LLD |
# |---|---|
# | Architecture | Object/class design |
# | Major components | Classes/interfaces |
# | Services | Objects |
# | Databases | Data structures/models |
# | Communication | Method interactions |
# | Scalability | Maintainability/extensibility |
# | Distributed systems | OOP/design principles |

# An API gateway acts as a single-entry point for client requests in a microservices architecture, handling routing, authentication, authorization, rate limiting,caching,etc
