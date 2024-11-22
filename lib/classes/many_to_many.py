import re
class NationalPark:
    all_national_parks = []
    def __init__(self, name):
        if not isinstance(name,str) or len(name)<3:
            raise ValueError("Name must be of type string and have 3 or more characters")
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not isinstance(name,str) or len(name)<3:
            raise ValueError("Name must be of type string and have 3 or more characters")
        if hasattr(self,'_name'):
            raise AttributeError("name cannot be changed after instantiation")
    def trips(self):
        return [trip for trip in self.all_national_parks if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    
    def total_visits(self):
        if (len(self.trips())==0):
            return 0
        return len(self.trips())
    def unique_visitors(self):
        unique_list = {trip.visitor for trip in self.all_national_parks}
        return unique_list
    
    def best_visitor(self):
        if not self.trips():
            return None
        visitor_counter = {}
        for trip in self.trips():
            if trip.visitor in visitor_counter:
                visitor_counter[trip.visitor] += 1
            else:
                visitor_counter[trip.visitor] = 1
        return max(visitor_counter, key=visitor_counter.get, default=None)

       




class Trip:
    all = []
    DATE_PATTERN = r"^(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(st|nd|rd|th)$"
    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(national_park,NationalPark):
            raise TypeError("national_park must be of type NationalPark")
        if not isinstance(visitor,Visitor):
            raise TypeError("visitor must be of type Visitor")
        if not isinstance(start_date,str) or len(start_date)<7 or not re.match(self.DATE_PATTERN,start_date):
            raise ValueError("start_date must be of type string and have 7 or more characters")
        
        if not isinstance(end_date,str) or len(end_date)<7 or not re.match(self.DATE_PATTERN,end_date):
            raise ValueError("end_date must be of type string and have 7 or more characters")
        Visitor.all_trips.append(self)
        NationalPark.all_national_parks.append(self)
        self.visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        Trip.all.append(self)
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self,start_date):
        if not isinstance(start_date,str) or len(start_date)<7 or not re.match(self.DATE_PATTERN,start_date):
            raise ValueError("start_date must be of type string and have 7 or more characters")
        self._start_date = start_date
    @property 
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self,end_date):
        if not isinstance(end_date,str) or len(end_date)<7 or not re.match(self.DATE_PATTERN,end_date):
            raise ValueError("end_date must be of type string and have 7 or more characters")
        self._end_date = end_date
        
    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self,visitor):
        if isinstance(visitor,Visitor):
            self._visitor = visitor
        else:
            raise TypeError("visitor must be of type Visitor")
    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self,national_park):
        if isinstance(national_park,NationalPark):
            self._national_park = national_park
        else:
            raise AttributeError("national_park must be of type NationalPark")
    


class Visitor:
    all_trips = []
    def __init__(self, name):
        if not isinstance(name,str) or len(name)<=0 or len(name)>15:
            raise ValueError("Name must be of type string and be between the length of 1 and 15 characters.")
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not isinstance(name,str) or len(name)<0 or len(name)>15:
            raise ValueError("Name must be of type string and be between the length of 1 and 15 characters.")
        
        self._name = name
    
        
    def trips(self):
        return [order for order in self.all_trips if order.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        obj1 = [visits for visits in self.all_trips if visits.national_park == self]
        return len(obj1)