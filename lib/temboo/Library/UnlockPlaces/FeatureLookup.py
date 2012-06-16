
###############################################################################
#
# FeatureLookup
# Searches for features by ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FeatureLookup(Choreography):

    """
    Create a new instance of the FeatureLookup Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/UnlockPlaces/FeatureLookup')


    def new_input_set(self):
        return FeatureLookupInputSet()

    def _make_result_set(self, result, path):
        return FeatureLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FeatureLookupChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FeatureLookup
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FeatureLookupInputSet(InputSet):
        """
        Set the value of the Format input for this choreography. ((optional, string) The format of the place search results. One of xml, kml, json, georss or txt. Defaults to "xml".)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the Gazetteer input for this choreography. ((optional, string) The place-name source to take locations from. The options are geonames, os, naturalearth or unlock which combines all the previous. Defaults to "unlock".)
        """
        def set_Gazetteer(self, value):
            InputSet._set_input(self, 'Gazetteer', value)

        """
        Set the value of the ID input for this choreography. ((required, integer) The ID of the feature you want to search for. Note that this identifier is returned in the <id> response element of the NameAndFeatureSearch Choreo.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the MaxRows input for this choreography. ((optional, integer) The maximum number of results to return. Defaults to 20. Cannot exceed 1000.)
        """
        def set_MaxRows(self, value):
            InputSet._set_input(self, 'MaxRows', value)

        """
        Set the value of the StartRow input for this choreography. ((optional, integer) The row to start results display from. Defaults to 1.)
        """
        def set_StartRow(self, value):
            InputSet._set_input(self, 'StartRow', value)


"""
A ResultSet with methods tailored to the values returned by the FeatureLookup choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FeatureLookupResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Unlock. Defaults to XML based on the format input parameter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FeatureLookupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FeatureLookupResultSet(response, path)
