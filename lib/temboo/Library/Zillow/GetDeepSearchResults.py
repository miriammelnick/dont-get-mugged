
###############################################################################
#
# GetDeepSearchResults
# Retrieve comprehensive property information for a specified address. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetDeepSearchResults(Choreography):

    """
    Create a new instance of the GetDeepSearchResults Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zillow/GetDeepSearchResults')


    def new_input_set(self):
        return GetDeepSearchResultsInputSet()

    def _make_result_set(self, result, path):
        return GetDeepSearchResultsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDeepSearchResultsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetDeepSearchResults
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetDeepSearchResultsInputSet(InputSet):
        """
        Set the value of the Address input for this choreography. ((required, string) Enter the address of the property to search.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the City input for this choreography. ((required, string) Enter a city name.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the RentEstimate input for this choreography. ((optional, boolean) Set to 1 (true) to enable. Defaults to 0 (false).)
        """
        def set_RentEstimate(self, value):
            InputSet._set_input(self, 'RentEstimate', value)

        """
        Set the value of the State input for this choreography. ((required, string) Enter a State abbreviation. If State is set, an entry for City must also be entered.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the ZWSID input for this choreography. ((required, string) Enter a Zillow Web Service Identifier (ZWS ID).)
        """
        def set_ZWSID(self, value):
            InputSet._set_input(self, 'ZWSID', value)

        """
        Set the value of the Zipcode input for this choreography. ((required, integer) Enter a zipcode. Can be combined with or without the  City and State input variables.)
        """
        def set_Zipcode(self, value):
            InputSet._set_input(self, 'Zipcode', value)


"""
A ResultSet with methods tailored to the values returned by the GetDeepSearchResults choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetDeepSearchResultsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zillow.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetDeepSearchResultsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDeepSearchResultsResultSet(response, path)
