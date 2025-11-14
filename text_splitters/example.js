// Sample JavaScript code for testing document structuring

// Class definition with methods
class UserManager {
    constructor() {
        this.users = [];
    }

    addUser(name, email, age) {
        const user = {
            id: Date.now(),
            name: name,
            email: email,
            age: age,
            createdAt: new Date()
        };
        this.users.push(user);
        return user;
    }

    findUserByEmail(email) {
        return this.users.find(user => user.email === email);
    }
}

// Nested object structure
const companyStructure = {
    name: "TechCorp",
    departments: {
        engineering: {
            head: "John Doe",
            teams: ["Frontend", "Backend", "DevOps"],
            employeeCount: 50,
            projects: {
                active: ["Project A", "Project B"],
                completed: ["Project X", "Project Y"]
            }
        },
        marketing: {
            head: "Jane Smith",
            teams: ["Digital", "Content", "PR"],
            employeeCount: 25
        }
    },
    locations: ["New York", "London", "Tokyo"]
};

// Async function with try-catch
async function fetchUserData(userId) {
    try {
        const response = await fetch(`https://api.example.com/users/${userId}`);
        if (!response.ok) {
            throw new Error('User not found');
        }
        const userData = await response.json();
        return userData;
    } catch (error) {
        console.error('Error fetching user:', error);
        return null;
    }
}

// Complex function with multiple conditions
function processUserPermissions(user, requestedAccess) {
    const basePermissions = {
        read: true,
        write: false,
        admin: false
    };

    if (user.role === 'admin') {
        return {
            ...basePermissions,
            write: true,
            admin: true,
            superUser: true
        };
    } else if (user.role === 'editor' && requestedAccess === 'content') {
        return {
            ...basePermissions,
            write: true,
            contentManager: true
        };
    }

    return basePermissions;
}

// Event handling example
document.addEventListener('DOMContentLoaded', () => {
    const userManager = new UserManager();
    
    // Example usage
    const newUser = userManager.addUser('Alice', 'alice@example.com', 28);
    console.log('New user created:', newUser);
    
    // Test permission system
    const userPermissions = processUserPermissions({ role: 'editor' }, 'content');
    console.log('User permissions:', userPermissions);
});