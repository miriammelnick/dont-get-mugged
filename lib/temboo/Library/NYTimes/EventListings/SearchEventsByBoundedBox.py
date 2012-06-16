
###############################################################################
#
# SearchEventsByBoundedBox
# Allows you to do a spatial search for events within a box bounded by specified northeast and southwest points.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchEventsByBoundedBox(Choreography):

    """
    Create a new instance of the SearchEventsByBoundedBox Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/EventListings/SearchEventsByBoundedBox')


    def new_input_set(self):
        return SearchEventsByBoundedBoxInputSet()

    def _make_result_set(self, result, path):
        return SearchEventsByBoundedBoxResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchEventsByBoundedBoxChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchEventsByBoundedBox
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchEventsByBoundedBoxInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the DateRange input for this choreography. ((optional, date) Start date to end date in the following format: YYYY-MM-DD:YYYY-MM-DD.)
        """
        def set_DateRange(self, value):
            InputSet._set_input(self, 'DateRange', value)

        """
        Set the value of the Filters input for this choreography. ((optional, string) Filters search results using facet names and values. See Choreo documentation for examples.)
        """
        def set_Filters(self, value):
            InputSet._set_input(self, 'Filters', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to return.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the NortheastLatitude input for this choreography. ((conditional, decimal) The northeastern latitude of the bounding box to search. When searching within a bounded box, all four coordinates are required.)
        """
        def set_NortheastLatitude(self, value):
            InputSet._set_input(self, 'NortheastLatitude', value)

        """
        Set the value of the NortheastLongitude input for this choreography. ((conditional, decimal) The northeastern longitude of the bounding box to search. When searching within a bounded box, all four coordinates are required.)
        """
        def set_NortheastLongitude(self, value):
            InputSet._set_input(self, 'NortheastLongitude', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) A numeric value indicating the starting point of the result set. This can be used in combination with the Limit input to page through results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) Search keywords to perform a text search on the following fields: web_description, event_name and venue_name.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Radius input for this choreography. ((optional, integer) The radius of the spacial search (in meters). Defaults to 1000.)
        """
        def set_Radius(self, value):
            InputSet._set_input(self, 'Radius', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to json, xml, or sphp. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) Allows you to sort results. Appending "+asc" or "+desc" to a facet will sort results on that value in ascending or descending order (i.e. dist+asc).)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)

        """
        Set the value of the SouthwestLatitude input for this choreography. ((conditional, decimal) The southwest latitude of the bounding box to search. When searching within a bounded box, all four coordinates are required.)
        """
        def set_SouthwestLatitude(self, value):
            InputSet._set_input(self, 'SouthwestLatitude', value)

        """
        Set the value of the SouthwestLongitude input for this choreography. ((conditional, decimal) The southwest longitude of the bounding box to search. When searching within a bounded box, all four coordinates are required.)
        """
        def set_SouthwestLongitude(self, value):
            InputSet._set_input(self, 'SouthwestLongitude', value)


"""
A ResultSet with methods tailored to the values returned by the SearchEventsByBoundedBox choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchEventsByBoundedBoxResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchEventsByBoundedBoxChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchEventsByBoundedBoxResultSet(response, path)
