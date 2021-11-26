class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        
        def checkValid(email):
            local, domain = email.split("@")
            
            left = ''
            for c in local:
                if c == '+':
                    break
                
                if c != '.':
                    left += c
            
            valid = left + '@' + domain
            return valid
                    
            
        for email in emails:
            uniqueEmails.add(checkValid(email))
            
        return len(uniqueEmails)